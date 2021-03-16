import mcpython.common.event.Registry
from mcpython import shared

import mcpython.common.block.Block
import mcpython.common.block.plugins.AbstractBlockPlugin


shared.block_registry = mcpython.common.event.Registry.Registry(
    "minecraft:block", mcpython.common.block.Block.Block
)
shared.block_plugin_registry = mcpython.common.event.Registry.Registry(
    "minecraft:block_plugins",
    mcpython.common.block.plugins.AbstractBlockPlugin.BlockPlugin,
)
