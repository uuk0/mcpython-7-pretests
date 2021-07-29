from abc import ABC
import mcpython.common.world.abstract


class AbstractWorldGenerationLayer(ABC):
    async def generate_in_chunk(
        self, chunk: mcpython.common.world.abstract.AbstractChunk
    ):
        raise NotImplementedError
