import json
import typing
from abc import ABC

import PIL.Image

from mcpython import shared
import os
import zipfile
import itertools

import mcpython.util.net


class AbstractResourceSource(ABC):
    def get_identifier(self) -> str:
        raise NotImplementedError

    def unload_links(self):
        pass

    def iterate(self, folder: str = "") -> typing.Iterator[str]:
        pass

    def exists(self, file: str) -> bool:
        raise NotImplementedError

    def read_raw(self, file: str) -> bytes:
        raise NotImplementedError

    def write_raw(self, file: str, data: bytes):
        raise NotImplementedError


class DirectorySource(AbstractResourceSource):
    def __init__(self, directory: str):
        self.directory = directory

    def get_identifier(self) -> str:
        return self.directory

    def iterate(self, folder: str = "") -> typing.Iterator[str]:
        for root, dirs, files in os.walk(folder):
            if not root.startswith(folder):
                continue

            # todo: maybe yield empty sub-folders also?
            yield root
            yield from map(
                lambda e: os.path.join(root, e)[len(self.directory) :], files
            )

    def exists(self, file: str) -> bool:
        return os.path.exists(os.path.join(self.directory, file))

    def read_raw(self, file: str) -> bytes:
        with open(os.path.join(self.directory, file), mode="rb") as f:
            return f.read()

    def write_raw(self, file: str, data: bytes):
        with open(os.path.join(self.directory, file), mode="wb") as f:
            f.write(data)


class ArchiveSource(AbstractResourceSource):
    def __init__(self, file: str):
        self.file = file
        self.archive = zipfile.ZipFile(file)

    def get_identifier(self) -> str:
        return self.file

    def unload_links(self):
        self.archive.close()

    def iterate(self, folder: str = "") -> typing.Iterator[str]:
        for e in self.archive.namelist():
            if e.startswith(folder):
                yield e

    def exists(self, file: str) -> bool:
        return file in self.archive.namelist()

    def read_raw(self, file: str) -> bytes:
        return self.archive.read(file)

    def write_raw(self, file: str, data: bytes):
        raise NotImplementedError


class InMemorySource(AbstractResourceSource):
    def __init__(self, name: str):
        self.name = name
        self.data = {}

    def get_identifier(self) -> str:
        return self.name

    def unload_links(self):
        self.data.clear()

    def iterate(self, folder: str = "") -> typing.Iterator[str]:
        yield from filter(lambda e: e.startswith(folder), self.data.keys())

    def read_raw(self, file: str) -> bytes:
        return self.data[file]

    def exists(self, file: str) -> bool:
        return file in self.data

    def write_raw(self, file: str, data: bytes):
        self.data[file] = data


class ResourceLocator:
    def __init__(self):
        self.sources = {}
        self.source_order = []

    def load_default_resources(self):
        if not os.path.exists(shared.local + "/source.zip"):
            print("downloading assets...")
            mcpython.util.net.download_file(
                shared.MC.ASSET_SOURCE_URL, shared.local + "/source_tmp.zip"
            )

            print("filtering sources...")

            # filter all non-asset sources from the file tree todo: use filter() on namelist

            with zipfile.ZipFile(
                shared.local + "/source_tmp.zip"
            ) as f, zipfile.ZipFile(shared.local + "/source.zip", mode="w") as wf:
                for file in f.namelist():
                    if file.endswith("/"):
                        continue

                    if ("assets/" in file or "data/" in file) and "net/" not in file:
                        with f.open(file, mode="r") as f1, wf.open(
                            file, mode="w"
                        ) as f2:
                            f2.write(f1.read())

            # remove the unfiltered file

            os.remove(shared.local + "/source_tmp.zip")

            print("finished!")

        self.add_source_archive(shared.local + "/source.zip")

    def add_source(self, source: AbstractResourceSource):
        print("loading asset source '" + str(source.get_identifier()) + "'")
        self.sources[source.get_identifier()] = source
        self.source_order.insert(0, source)

    def add_source_directory(self, directory: str):
        self.add_source(DirectorySource(directory))

    def add_source_archive(self, file: str):
        self.add_source(ArchiveSource(file))

    def iterate(self, directory: str = ""):
        items = itertools.chain(
            map(lambda locator: locator.iterate(directory), self.source_order)
        )
        yielded = set()
        for item in items:
            if item not in yielded:
                yielded.add(item)
                yield item

    def exists(self, file: str) -> bool:
        return any(locator.exists(file) for locator in self.source_order)

    def read_raw(self, file: str, default=None) -> bytes:
        for locator in self.source_order:
            if locator.exists(file):
                return locator.read_raw(file)
        return default

    def read_image(self, file: str) -> PIL.Image.Image:
        with open(shared.tmp.name + "/resource_locator_image.png", mode="wb") as f:
            f.write(self.read_raw(file))
        return PIL.Image.open(shared.tmp.name + "/resource_locator_image.png")

    def read_json(self, file: str):
        return json.loads(self.read_raw(file).decode("utf-8"))


shared.resource_locator = ResourceLocator()
