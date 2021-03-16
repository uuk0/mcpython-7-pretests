import typing
from abc import ABC


class AbstractCodec(ABC):
    def decode(self, data):
        raise NotImplementedError

    def encode(self, data, plugins=None):
        raise NotImplementedError

    def get_default_file_target(self, data) -> typing.Optional[str]:
        return


class AbstractEncodeAble(ABC):
    @classmethod
    def get_codec(cls) -> typing.Optional[AbstractCodec]:
        pass
