import multiprocessing
import sys
import threading
import marshal
import pickle
import traceback
import types
import typing

from mcpython import shared

CURRENT_HANDLER: typing.Optional["RemoteProcessHandler"] = None


def serialize_task(
    func: typing.Union[str, typing.Callable], args=tuple(), kwargs=None
) -> bytes:
    """
    Helper function for serializing tasks across processes
    :param func: the callable object, or a str to exec()
    :param args: the args to call with
    :param kwargs: the kwargs to call with
    :return: the bytes of the serialized task
    """
    return pickle.dumps(
        (
            marshal.dumps(func.__code__)
            if isinstance(func, types.FunctionType)
            else func,
            args,
            kwargs,
            (isinstance(func, types.LambdaType) and func.__name__ == "<lambda>"),
        )
    )


def deserialize_task(
    data: bytes,
) -> typing.Tuple[typing.Callable, typing.Iterable, typing.Optional[typing.Dict]]:
    """
    Deserializes a task
    :param data: the data to deserialize from
    :return: a tuple of a function invoking the code, and the args and optional kwargs to call with
    """
    if isinstance(data, tuple):
        data = data[0]
    assert isinstance(data, bytes), f"pickling will fail on provided data: {data}"

    code, args, kwargs, is_lambda = pickle.loads(data)
    if isinstance(code, bytes):
        code = marshal.loads(code)
        # print(code, args, kwargs, is_lambda)
        if not is_lambda:
            return types.FunctionType(code, globals()), args, kwargs
        return types.FunctionType(code, globals(), closure=tuple()), args, kwargs

    elif isinstance(code, str):
        return (
            lambda handler: exec(
                code,
                globals(),
                (
                    {"handler": handler} | kwargs
                    if kwargs is not None
                    else {"handler": handler}
                ),
            ),
            tuple(),
            None,
        )

    else:
        raise RuntimeError(f"Invalid code type: {type(code)} (data: {code})")


class RemoteProcessHandler:
    """
    Handler on the process side
    """

    def __init__(self, name: str):
        # The name of this process, for informal reasons
        self.name = name

        # A queue for tasks to execute here
        self.on_process_queue = multiprocessing.Queue()

        # A queue for tasks to execute somewhere else
        self.other_process_queue = multiprocessing.Queue()

        # A queue for stuff to be printed
        self.print_queue = multiprocessing.Queue()

        # If this process is still alive
        self.running = True

        # For rendering process: the window
        # todo: other processes may want some lazy getter system here
        self.window = None

    def print_safe(self, *args, **kwargs):
        self.print_queue.put((args, kwargs))

    def main(self):
        global CURRENT_HANDLER
        CURRENT_HANDLER = self
        shared.process_handler = self

        while self.running:
            self.fetch()

    def fetch(self, dt=None):
        while not self.on_process_queue.empty():
            target = deserialize_task(self.on_process_queue.get())
            try:
                if target[2] is None:
                    target[0](self, *target[1])
                else:
                    target[0](self, *target[1], **target[2])
            except SystemExit:
                raise
            except:
                print(target)
                traceback.print_exc()

    def async_workflow(self):
        global CURRENT_HANDLER
        CURRENT_HANDLER = self
        shared.process_handler = self

        import asyncio

        asyncio.run(self.async_main())

    async def async_main(self):
        while True:
            await self.fetch_async()

    async def fetch_async(self):
        while not self.on_process_queue.empty():
            target = deserialize_task(self.on_process_queue.get())
            try:
                if target[2] is None:
                    t = target[0](self, *target[1])
                else:
                    t = target[0](self, *target[1], **target[2])

                # todo: can we do better than this?
                try:
                    await t
                except TypeError:
                    pass
            except SystemExit:
                raise

            except:
                traceback.print_exc()
                # todo: decide if to exit or not!

    def execute_on(
        self,
        process_name: str,
        task: typing.Union[typing.Callable, str],
        *args,
        **kwargs,
    ):
        """
        Executes a task on another process
        If the other process is this process, the task will be inserted directly into the local pipe
        :param process_name: the name of the process
        :param task: the callable or source code of the task
        :param args: the args
        :param kwargs: the kwargs
        """
        data = (serialize_task(task, args, kwargs if len(kwargs) > 0 else None),)
        if process_name == self.name:
            self.on_process_queue.put(data)
        else:
            self.other_process_queue.put((process_name, data))

    def stop(self, exit_code=0):
        """
        Stops the execution immediately. Will raise SystemExit, DO NOT HANDLE
        :param exit_code: the exit code
        """

        print("stopping game from process", self.name, "with exit code", exit_code)
        self.execute_on(
            "main",
            lambda: __import__("mcpython.ProcessManager").ProcessManager.execute_on_all(
                lambda handler: handler.this_stop()
            ),
        )
        self.execute_on("main", lambda code: __import__("sys").exit(code), exit_code)
        sys.exit()

    def this_stop(self):
        """
        Internal use only
        Used to stop THIS process, not the other ones
        Use stop() for stopping all (including this)
        """
        print("stopping process", self.name)
        self.running = False
        sys.exit()

    def set_flag(self, name: str):
        self.print_safe(f"setting flag '{name}' to 'True'")
        FLAGS[name] = True

    def unset_flag(self, name: str):
        self.print_safe(f"setting flag '{name}' to 'False'")
        FLAGS[name] = False

    def has_flag(self, name: str) -> bool:
        return FLAGS.setdefault(name, False)


def spawn_process(name: str, target=None, async_process=False):
    """
    Spawns a new process with name <name>, with main loop function <target> (defaults to a normal loop when
        <async_process> is False, otherwise a async handling loop)
    """

    handler = RemoteProcessHandler(name)
    if async_process:
        process = multiprocessing.Process(target=handler.async_workflow)
    else:
        process = multiprocessing.Process(
            target=handler.main if target is not None else handler.fetch
        )

    handler.on_process_queue.put(
        serialize_task(
            """
import mcpython.ProcessManager
mcpython.ProcessManager.FLAGS = flags""",
            kwargs={"flags": FLAGS},
        )
    )

    if target is not None:
        handler.on_process_queue.put(serialize_task(target))

    PROCESSES[name] = process
    PROCESS_HANDLERS[name] = handler

    return handler


def start_processes():
    """
    Starts all arrival processes
    """

    for process in PROCESSES.values():
        process.start()


def maintain():
    """
    Maintain handler loop
    Will loop until stop is scheduled from a process
    This loop is needed in order for cross-process data sync to work
    """

    while True:
        # Iterate over all processes
        for handler in PROCESS_HANDLERS.values():
            # Fetch all tasks
            while not handler.other_process_queue.empty():
                target_process, data = handler.other_process_queue.get()

                # If it is scheduled here, execute it here
                if target_process == "main":
                    func, args, kwargs = deserialize_task(data)

                    # todo: try-except
                    if kwargs is not None:
                        func(*args, **kwargs)
                    else:
                        func(*args)

                # Otherwise, send it to the process
                elif target_process in PROCESS_HANDLERS:
                    # todo: check for name existence
                    PROCESS_HANDLERS[target_process].on_process_queue.put(data)
                else:
                    print(
                        f"[PROCESS MANAGER][FATAL] failed to send task to process '{target_process}', as it was never spawned"
                    )

            # This is a queue for printing stuff on the main process
            while not handler.print_queue.empty():
                args, kwargs = handler.print_queue.get()
                print(*args, **kwargs)

        # And lookout for exits todo: add special flag variable
        for process in PROCESSES.values():
            if process.exitcode:
                print("stopping game from main thread")
                for name in PROCESSES:
                    print(" - killing", name)
                    PROCESSES[name].kill()

                return


PROCESSES: typing.Dict[str, multiprocessing.Process] = {}
PROCESS_HANDLERS: typing.Dict[str, RemoteProcessHandler] = {}
MANAGER = None
FLAGS: typing.Optional[dict] = None


def setup_dict():
    global MANAGER, FLAGS
    MANAGER = multiprocessing.Manager()
    FLAGS = MANAGER.dict()


# Only for main process work
def execute_on(process: str, func, *args, **kwargs):
    PROCESS_HANDLERS[process].on_process_queue.put(
        serialize_task(func, args, kwargs if len(kwargs) > 0 else None)
    )


def execute_on_all(func, *args, **kwargs):
    task = serialize_task(func, args, kwargs if len(kwargs) > 0 else None)
    for handler in PROCESS_HANDLERS.values():
        handler.on_process_queue.put(task)
