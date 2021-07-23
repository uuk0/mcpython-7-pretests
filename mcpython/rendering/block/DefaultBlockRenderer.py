import mcpython.rendering.block.AbstractBlockRenderer
import mcpython.common.block.BlockState
import mcpython.rendering.block.ChunkSectionCache

import mcpython.rendering.block.BlockRenderingManager


@mcpython.rendering.block.BlockRenderingManager.BLOCK_RENDERER_REGISTRY.register
class DefaultBlockRenderer(
    mcpython.rendering.block.AbstractBlockRenderer.AbstractBlockRenderer
):
    """
    Default implementation for block rendering
    Uses the common API at Block(State)
    Registered under
    """

    NAME = "minecraft:default_block_renderer"

    def add_block_to_section(
        self,
        block_state: mcpython.common.block.BlockState.BlockState,
        cache: mcpython.rendering.block.ChunkSectionCache.ChunkSectionCache,
    ):
        pass  # todo: implement
