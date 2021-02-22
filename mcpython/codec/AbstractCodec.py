from abc import ABC


class AbstractCodec(ABC):
    def decode(self, data):
        raise NotImplementedError

    def encode(self, data):
        raise NotImplementedError

