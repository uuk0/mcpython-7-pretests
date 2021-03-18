import traceback
import typing
import simplejson

from mcpython.data.codec.AbstractCodec import AbstractCodec


class CodecArgSource:
    @classmethod
    def from_any(cls, source) -> "CodecArgSource":
        if isinstance(source, CodecArgSource):
            return source

        if isinstance(source, str):
            return cls().add_dict_entry_get(source)

        if isinstance(source, (tuple, list)):
            return cls().add_dict_entry_get(*source)

        raise NotImplementedError(source)

    def __init__(self):
        self.tree = []

    def add_dict_entry_get(self, *keys: str) -> "CodecArgSource":
        self.tree += keys
        return self

    def add_codec_list(self, codec: AbstractCodec):
        pass

    def add_conditional_codec(
        self, codec: AbstractCodec, condition: typing.Callable[[typing.Any], bool]
    ):
        pass

    def decode_from(self, data_tree: dict):
        for key in self.tree:
            data_tree = data_tree[key]

        return data_tree

    def encode_into(self, entry, data_tree: dict):
        for key in self.tree[:-1]:
            data_tree = data_tree.setdefault(key, {})

        data_tree[self.tree[-1]] = entry


class Codec(AbstractCodec):
    def __init__(
        self,
        obj_creator: typing.Callable,
        obj_handler: typing.Callable = None,
        base_decoder=lambda data: simplejson.loads(data.decode("utf-8")),
        # Default json encoder; good look and sorted keys for same order across builds
        base_encoder=lambda data: simplejson.dumps(data, indent="  ", sort_keys=True).encode("utf-8"),
        file_target_formatting: typing.Callable[[typing.Any], str] = None,
    ):
        """
        Creates a new codec instance
        :param obj_creator: A callable where serialized data can be decoded into
        :param obj_handler: A callable called with the encoded object
        :param base_decoder: handles the raw data and converts it into something readable, defaults to json
        :param base_encoder: the other way round of base_decoder, uses json per default, with good formatting
        :param file_target_formatting: A callable formatting a object name into a file path
        """
        self.obj_creator = obj_creator
        self.obj_handler = obj_handler
        self.base_decoder = base_decoder
        self.base_encode = base_encoder

        self.file_target_formatting = file_target_formatting

        self.arguments = [], {}
        self.attributes = {}

    def register_list_argument(
        self,
        source,
        converter: typing.Callable = None,
        validator: typing.Callable[[typing.Any], bool] = None,
    ):
        self.arguments[0].append(
            (
                CodecArgSource.from_any(source),
                converter,
                validator,
            )
        )
        return self

    def register_keyword_argument(
        self,
        source,
        name: str,
        converter: typing.Callable = None,
        validator: typing.Callable[[typing.Any], bool] = None,
    ):
        self.arguments[1][name] = (
            CodecArgSource.from_any(source),
            converter,
            validator,
        )
        return self

    def register_attribute_setter(
        self,
        source,
        attr_name: str,
        converter_from_data: typing.Callable = None,
        converter_from_obj: typing.Callable = None,
        validator: typing.Callable[[typing.Any], bool] = None,
        on_serialize=True,
        on_deserialize=True,
        serialize_only_if: typing.Callable[[typing.Any], bool] = None,
    ):
        self.attributes[attr_name] = (
            CodecArgSource.from_any(source),
            converter_from_data,
            converter_from_obj,
            validator,
            on_serialize,
            on_deserialize,
            serialize_only_if,
        )
        return self

    def decode(self, data):
        if isinstance(data, bytes):
            data = self.base_decoder(data)

        args = []
        for source, converter, validator in self.arguments[0]:
            d = source.decode_from(data)

            if d is not None:
                if converter is not None:
                    d = converter(d)

                assert validator(d)

                args.append(d)

        kwargs = {}
        for name, (source, converter, validator) in self.arguments[1].items():
            d = source.decode_from(data)
            if d is None:
                continue

            d = converter(d)
            assert validator(d)
            kwargs[name] = d

        obj = self.obj_creator(*args, **kwargs)

        for name, (
            source,
            converter,
            _,
            validator,
            __,
            on_deserialize,
            ___,
        ) in self.attributes.items():
            if not on_deserialize:
                continue

            d = source.decode_from(data)
            if d is None:
                continue

            d = converter(d)
            assert validator(d)

            setattr(obj, name, d)

        if self.obj_handler:
            self.obj_handler(obj)

        return obj

    def encode(self, obj, plugins=None):
        data = {"plugins": plugins} if plugins is not None else {}
        for name, (
            source,
            _,
            converter,
            validator,
            on_serialize,
            __,
            serialize_if,
        ) in self.attributes.items():
            if not hasattr(obj, name) or not on_serialize:
                continue
            d = getattr(obj, name)

            if callable(serialize_if) and not serialize_if(d):
                continue

            if callable(converter):
                d = converter(d)

            if callable(validator):
                assert validator(d)

            source.encode_into(d, data)

        return self.base_encode(data)

    def get_default_file_target(self, obj):
        return None if self.file_target_formatting is None else self.file_target_formatting(obj)
