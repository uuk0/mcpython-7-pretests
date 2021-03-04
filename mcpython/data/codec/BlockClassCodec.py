import mcpython.data.codec.ObjectConstructionCodec
import mcpython.common.block.Block


"""
First Codec instance ever created with the new system
Wraps the Block-class around a Codec for serialization

This is the first codec implemented, it might be completely broken...
"""
BLOCK_CODEC = (
    mcpython.data.codec.ObjectConstructionCodec.Codec(mcpython.common.block.Block.Block)
    .register_list_argument("name", validator=lambda value: isinstance(value, str))
    .register_keyword_argument(
        ("properties", "destroyed_by_explosion"),
        "destroyed_by_explosion",
        validator=lambda value: isinstance(value, bool),
    )
    .register_keyword_argument(
        ("properties", "destroyed_by_player"),
        "destroyed_by_player",
        validator=lambda value: isinstance(value, bool),
    )
    .register_keyword_argument(
        ("properties", "default_model_state"),
        "default_model_state",
        validator=lambda value: isinstance(value, dict),
    )
    .register_attribute_setter(("name",), "name", on_deserialize=False)
    # And now, the serializers for above...
    .register_attribute_setter(
        ("properties", "destroyed_by_explosion"),
        "destroyed_by_explosion",
        on_deserialize=False,
        serialize_only_if=lambda value: not value,
    )
    .register_attribute_setter(
        ("properties", "destroyed_by_player"),
        "destroyed_by_player",
        on_deserialize=False,
        serialize_only_if=lambda value: not value,
    )
    .register_attribute_setter(
        ("properties", "default_model_state"),
        "default_model_state",
        serialize_only_if=lambda value: len(value) > 0,
    )
)
