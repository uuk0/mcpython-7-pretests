import typing
import json

from mcpython.codec.AbstractCodec import AbstractCodec


class CodecArgSource:
    @classmethod
    def from_any(cls, source) -> "CodecArgSource":
        if isinstance(source, CodecArgSource):
            return source

    def __init__(self):
        pass

    def add_dict_entry_get(self, key: str, optional):
        pass

    def add_codec_list(self, codec: AbstractCodec):
        pass

    def add_conditional_codec(self, codec: AbstractCodec, condition: typing.Callable[[typing.Any], bool]):
        pass

    def decode_from(self, data_tree: dict):
        pass


class Codec(AbstractCodec):
    def __init__(
        self,
        obj_creator: typing.Callable,
        obj_handler: typing.Callable = None,
        base_decoder=lambda data: json.loads(data.decode("utf-8")),
    ):
        self.obj_creator = obj_creator
        self.obj_handler = obj_handler
        self.base_decoder = base_decoder

        self.arguments = [], {}
        self.attributes = {}

    def register_list_argument(self, source, converter: typing.Callable = None):
        self.arguments[0].append((CodecArgSource.from_any(source), converter))
        return self

    def register_keyword_argument(
        self, source, name: str, converter: typing.Callable = None
    ):
        self.arguments[1][name] = (CodecArgSource.from_any(source), converter)
        return self

    def register_attribute_setter(
        self, source, attr_name: str, converter: typing.Callable = None
    ):
        self.attributes[attr_name] = (CodecArgSource.from_any(source), converter)
        return self

    def decode(self, data):
        if isinstance(data, bytes):
            data = self.base_decoder(data)

        args = []
        for source, converter in self.arguments[0]:
            d = source.decode_from(data)

            if d is not None:
                if converter is not None:
                    d = converter(d)
                args.append(d)
