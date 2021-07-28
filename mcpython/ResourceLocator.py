import os
import typing
import zipfile
from abc import ABC


class AbstractResourceLookupLocation(ABC):
    def exists(self, file: str) -> bool:
        return False

    def load(self, file: str) -> bytes:
        raise FileNotFoundError

    def store(self, file: str, content: bytes):
        raise RuntimeError

    def walk(self, directory: str) -> typing.Iterable[str]:
        return tuple()

    def close(self):
        pass


class ResourceDirectoryLookup(AbstractResourceLookupLocation):
    def __init__(self, path: str):
        self.path = path

    def exists(self, file: str) -> bool:
        return os.path.exists(os.path.join(self.path, file))

    def load(self, file: str):
        with open(os.path.join(self.path, file), mode="rb") as f:
            return f.read()

    def store(self, file: str, content: bytes):
        with open(os.path.join(self.path, file), mode="wb") as f:
            f.write(content)

    def walk(self, directory: str) -> typing.Iterable[str]:
        for root, files, _ in os.walk(os.path.join(self.path, directory)):
            yield root[len(self.path)+1:]+"/"
            yield from (os.path.join(root, e)[len(self.path)+1:] for e in files)


class ResourceZipfileLookup(AbstractResourceLookupLocation):
    def __init__(self, path: str):
        self.path = zipfile.ZipFile(path)
        self.namelist = set(self.path.namelist())

    def close(self):
        self.path.close()

    def exists(self, file: str) -> bool:
        return file in self.namelist

    def load(self, file: str):
        return self.path.read(file)

    def store(self, file: str, content: bytes):
        self.namelist.add(file)
        self.path.writestr(file, content)

    def walk(self, directory: str) -> typing.Iterable[str]:
        yield from self.namelist


class ResourceManager:
    def __init__(self):
        self.static_lookups: typing.List[AbstractResourceLookupLocation] = []
        self.session_lookups: typing.List[AbstractResourceLookupLocation] = []
        self.lookups: typing.List[AbstractResourceLookupLocation] = []

    def add_static_resource_lookup(self, lookup: AbstractResourceLookupLocation):
        self.static_lookups.append(lookup)
        self.lookups.append(lookup)

    def add_session_resource_lookup(self, lookup: AbstractResourceLookupLocation):
        self.session_lookups.append(lookup)
        self.lookups.append(lookup)

    def close_session(self):
        for look in self.session_lookups:
            self.lookups.remove(look)
            look.close()
        self.session_lookups.clear()

    def close_all(self):
        for look in self.lookups:
            look.close()
        self.lookups.clear()
        self.static_lookups.clear()
        self.session_lookups.clear()

    def get_lookup_for_file(self, file: str) -> AbstractResourceLookupLocation:
        for lookup in self.lookups:
            if lookup.exists(file):
                return lookup

    def exists(self, file: str):
        return self.get_lookup_for_file(file) is not None

    def read(self, file: str):
        return self.get_lookup_for_file(file).load(file)

    def read_to_file(self, file: str, output: str):
        with open(output, mode="wb") as f:
            f.write(self.read(file))

    def walk(self, directory: str):
        for lookup in self.lookups:
            yield from lookup.walk(directory)


async def setup_side(_):
    from mcpython import shared, ResourceLocator

    shared.resource_manager = ResourceLocator.ResourceManager()
    shared.resource_manager.add_static_resource_lookup(ResourceLocator.ResourceZipfileLookup(shared.local+"/source.zip"))

