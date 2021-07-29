import typing
from abc import ABC

import mcpython.server.worldgen.layers.AbstractWorldGenerationLayer
import mcpython.common.world.abstract


class AbstractChunkGenerator(ABC):
    """
    ChunkGenerator is a class generating chunks in a dimension

    Implementations beside the default ChunkGenerator are allowed, make sure to implement
    generate_chunk
    """

    async def generate_chunk(self, chunk: mcpython.common.world.abstract.AbstractChunk):
        raise NotImplementedError


class ChunkGenerator(AbstractChunkGenerator):
    """
    The default chunk generator
    Wrapping the AbstractWorldGenerationLayer class around some internal structure
    """

    def __init__(self, name: str):
        self.name = name

        self.layers: typing.List[
            mcpython.server.worldgen.layers.AbstractWorldGenerationLayer.AbstractWorldGenerationLayer
        ] = []

    def add_layer(
        self,
        layer: mcpython.server.worldgen.layers.AbstractWorldGenerationLayer.AbstractWorldGenerationLayer,
    ):
        self.layers.append(layer)
        return self

    async def generate_chunk(self, chunk: mcpython.common.world.abstract.AbstractChunk):
        for layer in self.layers:
            await layer.generate_in_chunk(chunk)
        chunk.generated = True
