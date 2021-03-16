import os
import typing

import mcpython.data.codec.AbstractCodec


class DataGenerationDriver:
    def __init__(self):
        self.targets: typing.List[
            typing.Tuple[mcpython.data.codec.AbstractCodec.AbstractEncodeAble, typing.Optional[list]]
        ] = []

    def add_target(self, obj: mcpython.data.codec.AbstractCodec.AbstractEncodeAble, plugins=None):
        self.targets.append((obj, plugins))
        return self

    def work(self):
        for target, plugins in self.targets:
            # todo: do work
            print("running data generation entry for", target)
            codec = target.get_codec()
            if codec is None:
                print("NO CODEC FOUND, SKIPPING!")
                continue

            data = codec.encode(target, plugins=plugins)
            file = codec.get_default_file_target(target)

            if file is None:
                print("skipping dump to file system")
                continue

            d = os.path.dirname(file)

            if not os.path.isdir(d):
                os.makedirs(d)

            with open(file, mode="wb") as f:
                f.write(data)


driver = DataGenerationDriver()


def work_vanilla():
    from mcpython.data.gen import blocks

    driver.work()
