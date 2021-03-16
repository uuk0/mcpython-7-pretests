import mcpython.data.codec.ObjectConstructionCodec
import mcpython.common.block.Block


"""
First Codec instance ever created with the new system
Wraps the Block-class around a Codec for serialization

This is the first codec implemented, it might be completely broken...
"""
BLOCK_CODEC = (
    mcpython.data.codec.ObjectConstructionCodec.Codec(
        mcpython.common.block.Block.Block,
        file_target_formatting=lambda obj: "data/{}/registry/block/{}.json".format(*obj.name.split(":"))
    )
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
        on_deserialize=False,
        serialize_only_if=lambda value: len(value) > 0,
    )
    .register_attribute_setter(
        "name",
        "name",
        on_deserialize=False,
    )
    # And now, both directional stuff
    .register_attribute_setter(
        ("properties", "material"),
        "material",
        serialize_only_if=lambda value: value is not None
    )
    .register_attribute_setter(
        ("properties", "map_color"),
        "map_color",
        serialize_only_if=lambda value: value is not None
    )
    .register_attribute_setter(
        ("properties", "requires_tool"),
        "requires_tool",
        serialize_only_if=lambda value: value
    )
    .register_attribute_setter(
        ("properties", "hardness"),
        "hardness",
        serialize_only_if=lambda value: value != 0
    )
    .register_attribute_setter(
        ("properties", "blast_resistance"),
        "blast_resistance",
        serialize_only_if=lambda value: value != 0
    )
    .register_attribute_setter(
        ("properties", "ticks_randomly"),
        "ticks_randomly",
        serialize_only_if=lambda value: value
    )
    .register_attribute_setter(
        ("properties", "sound_group"),
        "sound_group",
        serialize_only_if=lambda value: value is not None
    )
    .register_attribute_setter(
        ("properties", "has_collision"),
        "has_collision",
        serialize_only_if=lambda value: not value
    )
    .register_attribute_setter(
        ("properties", "breaks_instantly"),
        "breaks_instantly",
        serialize_only_if=lambda value: value
    )
    .register_attribute_setter(
        ("properties", "drops_nothing"),
        "drops_nothing",
        serialize_only_if=lambda value: value
    )
    .register_attribute_setter(
        ("properties", "opaque"),
        "opaque",
        serialize_only_if=lambda v: not v
    )
    .register_attribute_setter(
        ("properties", "solid"),
        "solid",
        serialize_only_if=lambda v: not v
    )
    .register_attribute_setter(
        ("properties", "allow_spawns"),
        "allow_spawns",
        serialize_only_if=lambda v: not v
    )
    .register_attribute_setter(
        ("properties", "do_suffocation"),
        "do_suffocation",
        serialize_only_if=lambda v: not v
    )
    .register_attribute_setter(
        ("properties", "blocks_vision"),
        "blocks_vision",
        serialize_only_if=lambda v: not v
    )
    .register_attribute_setter(
        ("properties", "dynamic_bounds"),
        "dynamic_bounds",
        serialize_only_if=lambda v: v
    )
    .register_attribute_setter(
        ("properties", "drops_like"),
        "drops_like",
        serialize_only_if=lambda v: v is not None
    )
)
