import typing
import numpy as np
import mcpython.common.block.Block
import mcpython.common.block.BlockState


class ChunkSector:
    """
    A 16x16x16 region of the world
    """

    def __init__(self):
        self.chunk: typing.Optional["Chunk"] = None
        self.y_section: typing.Optional[int] = None
        self.blocks = np.empty(16 ** 3)
        self.dirty = False

    def get_block(
        self, position: typing.Tuple[int, int, int]
    ) -> typing.Optional[mcpython.common.block.BlockState.BlockState]:
        x, y, z = position
        cx, cz = self.chunk.position
        return self.get_block_relative(
            (x - cx * 16, y - self.y_section * 16, z - cz * 16)
        )

    def get_block_relative(
        self, position: typing.Tuple[int, int, int]
    ) -> typing.Optional[mcpython.common.block.BlockState.BlockState]:
        assert all(0 <= e < 16 for e in position), "relative position out of range"

        return self.blocks[position[0] + position[2] * 16 + position[1] * 256]

    def set_block(self, position: typing.Tuple[int, int, int], block):
        x, y, z = position
        cx, cz = self.chunk.position
        return self.set_block_relative(
            (x - cx * 16, y - self.y_section * 16, z - cz * 16), block
        )

    def set_block_relative(self, position: typing.Tuple[int, int, int], block):
        assert all(0 <= e < 16 for e in position), "relative position out of range"

        self.blocks[position[0] + position[2] * 16 + position[1] * 256] = block
        self.dirty = True


class Chunk:
    def __init__(self):
        # The dimension
        self.dimension = None

        # y -> ChunkSector
        self.sections: typing.Dict[int, ChunkSector] = {}

        # The entities
        self.entities = set()

        # Constants
        self.position: typing.Optional[typing.Tuple[int, int]] = None
        self.loaded = False
        self.generated = False

    def generate(self):
        if self.generated:
            return

    def load_from_saves(self):
        if self.loaded or self.generated:
            return

    def get_sector(self, y: int) -> ChunkSector:
        if y not in self.sections:
            sector = ChunkSector()
            sector.chunk = self
            sector.y_section = y
            sector.dirty = True
            return self.sections.setdefault(y, sector)

        return self.sections[y]

    def get_sector_for_position(self, position: tuple) -> ChunkSector:
        return self.get_sector(position[1] // 16)

    def get_block(
        self, position: typing.Tuple[int, int, int]
    ) -> typing.Optional[mcpython.common.block.BlockState.BlockState]:
        return self.get_sector_for_position(position).get_block(position)

    def get_block_relative(
        self, position: typing.Tuple[int, int, int]
    ) -> typing.Optional[mcpython.common.block.BlockState.BlockState]:
        y = position[1] // 16
        return self.get_sector(y).get_block_relative((position[0], y, position[2]))
