import multiprocessing
import threading
import marshal
import pickle
import typing


def serialize_task(func, args, kwargs) -> bytes:
    pass


def deserialize_task(data: bytes) -> typing.Tuple[typing.Callable, typing.List, typing.Dict]:
    pass


class RemoteProcessHandler:
    def __init__(self, name: str):
        self.name = name
        self.on_process_queue = multiprocessing.Queue()
        self.other_process_queue = multiprocessing.Queue()

    def main(self):
        while True:
            self.fetch()

    def fetch(self):
        pass

    def execute_on(self, process_name: str, task, *args, **kwargs):
        pass


def handler_process():
    pass


def spawn_process(name: str):
    process = multiprocessing.Process()
    handler = RemoteProcessHandler(name)
    PROCESSES[name] = process
    PROCESS_HANDLERS[name] = handler


PROCESSES = {}
PROCESS_HANDLERS = {}

