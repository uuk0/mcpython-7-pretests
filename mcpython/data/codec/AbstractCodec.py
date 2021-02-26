import typing
from abc import ABC


class AbstractCodec(ABC):
    def decode(self, data):
        raise NotImplementedError

    def encode(self, data):
        raise NotImplementedError


class AbstractEncodeAble(ABC):
    CODEC: typing.Optional[AbstractCodec] = None
