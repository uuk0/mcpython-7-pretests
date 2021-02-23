import multiprocessing
import threading
import marshal
import pickle
import traceback
import types
import typing


def serialize_task(func, args=tuple(), kwargs=None) -> bytes:
    return pickle.dumps((marshal.dumps(func.__code__), args, kwargs))


def deserialize_task(
    data: bytes,
) -> typing.Tuple[typing.Callable, typing.List, typing.Optional[typing.Dict]]:
    code, args, kwargs = pickle.loads(data)
    code = marshal.loads(code)
    return types.FunctionType(code, globals()), args, kwargs


class RemoteProcessHandler:
    def __init__(self, name: str):
        self.name = name
        self.on_process_queue = multiprocessing.Queue()
        self.other_process_queue = multiprocessing.Queue()
        self.running = True

    def main(self):
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
            except:
                print(target)
                traceback.print_exc()

    def async_workflow(self):
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

            except:
                print(target)
                traceback.print_exc()

    def execute_on(self, process_name: str, task, *args, **kwargs):
        self.other_process_queue.put(
            (
                process_name,
                serialize_task(task, args, kwargs if len(kwargs) > 0 else None),
            )
        )

    def stop(self):
        print("stopping game from process", self.name)
        self.execute_on(
            "main",
            lambda: __import__("mcpython.ProcessManager").ProcessManager.execute_on_all(
                lambda handler: handler.this_stop()
            ),
        )
        self.execute_on("main", lambda: __import__("sys").exit())

    def this_stop(self):
        self.running = False


def spawn_process(name: str, target=None, async_process=False):
    handler = RemoteProcessHandler(name)
    if async_process:
        process = multiprocessing.Process(target=handler.async_workflow)
    else:
        process = multiprocessing.Process(
            target=handler.main if target is not None else handler.fetch
        )

    if target is not None:
        handler.on_process_queue.put(serialize_task(target))

    PROCESSES[name] = process
    PROCESS_HANDLERS[name] = handler


def start_processes():
    for process in PROCESSES.values():
        process.start()


def maintain():
    while True:
        for handler in PROCESS_HANDLERS.values():
            while not handler.other_process_queue.empty():
                target_process, data = handler.other_process_queue.get()
                if target_process == "main":
                    func, args, kwargs = deserialize_task(data)

                    # todo: try-except
                    if kwargs is not None:
                        func(*args, **kwargs)
                    else:
                        func(*args)
                else:
                    # todo: check for name existence
                    PROCESS_HANDLERS[target_process].on_process_queue.put(data)

        for process in PROCESSES.values():
            if not process.is_alive():
                break
        else:
            continue


PROCESSES: typing.Dict[str, multiprocessing.Process] = {}
PROCESS_HANDLERS: typing.Dict[str, RemoteProcessHandler] = {}


# Only for main process work
def execute_on(process: str, func, *args, **kwargs):
    PROCESS_HANDLERS[process].on_process_queue.put(
        serialize_task(func, args, kwargs if len(kwargs) > 0 else None)
    )


def execute_on_all(func, *args, **kwargs):
    task = serialize_task(func, args, kwargs if len(kwargs) > 0 else None)
    for handler in PROCESS_HANDLERS.values():
        handler.on_process_queue.put(task)
