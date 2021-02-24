import mcpython.codec.ObjectConstructionCodec
import mcpython.common.block.Block


"""
First Codec instance ever created with the new system
Wraps the Block-class around a Codec for serialization
"""
BLOCK_CODEC = (
    mcpython.codec.ObjectConstructionCodec.Codec(mcpython.common.block.Block.Block)
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
)
