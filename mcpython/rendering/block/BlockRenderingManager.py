import typing

import mcpython.rendering.block.AbstractBlockRenderer
import mcpython.common.event.Registry


class BlockRenderingManager:
    def __init__(self):
        self.block2renderer: typing.Dict[
            str, mcpython.rendering.block.AbstractBlockRenderer.AbstractBlockRenderer
        ] = {}

    def set_special_renderer(
        self,
        block: str,
        renderer: mcpython.rendering.block.AbstractBlockRenderer.AbstractBlockRenderer,
    ):
        self.block2renderer[block] = renderer
        return self

    def setup(self):
        from mcpython.rendering.block import DefaultBlockRenderer


manager = BlockRenderingManager()

# The registry for all block renderers, for making them data-driveable
BLOCK_RENDERER_REGISTRY = mcpython.common.event.Registry.Registry(
    "minecraft:block_renderers",
    mcpython.rendering.block.AbstractBlockRenderer.AbstractBlockRenderer,
    target_is_class=True,
)
