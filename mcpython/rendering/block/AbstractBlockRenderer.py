import abc
import mcpython.common.event.Registry
import mcpython.common.block.BlockState
import mcpython.rendering.block.ChunkSectionCache


class AbstractBlockRenderer(mcpython.common.event.Registry.IRegistryContent, abc.ABC):
    """
    Abstract class for block renderers, defining how to render stuff
    """

    def add_block_to_section(
        self,
        block_state: mcpython.common.block.BlockState.BlockState,
        cache: mcpython.rendering.block.ChunkSectionCache.ChunkSectionCache,
    ):
        raise NotImplementedError
