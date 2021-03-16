import typing

import mcpython.rendering.block.AbstractBlockRenderer


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

    def update_chunk_section_render(self):
        pass


manager = BlockRenderingManager()
