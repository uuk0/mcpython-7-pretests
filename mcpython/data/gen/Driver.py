import typing

import mcpython.data.codec.AbstractCodec


class DataGenerationDriver:
    def __init__(self):
        self.targets: typing.List[mcpython.data.codec.AbstractCodec.AbstractEncodeAble] = []

    def add_target(self, obj: mcpython.data.codec.AbstractCodec.AbstractEncodeAble):
        self.targets.append(obj)
        return self

    def work(self):
        for target in self.targets:
            # todo: do work
            pass


driver = DataGenerationDriver()

