import typing
from abc import ABC


BLOCK_POSITION = typing.Tuple[int, int, int]
CHUNK_POSITION = typing.Tuple[int, int]


class UnableToLoadChunkException(Exception):
    pass


class UnableToPlaceBlockException(Exception):
    pass


class UnableToFindBlockException(Exception):
    pass


class AbstractBlockAccess(ABC):
    """
    Common base class across Chunk and Dimension, as both allow
    direct access to the data structure storing the block information

    Can be used in cases where both are allowed, e.g. small world generation functions

    WARNING: using chunks can lead into problems when a position is outside the chunk range
    """

    async def add_block(
        self,
        position: BLOCK_POSITION,
        block_type,
        meta=None,
        invoke_block_updates=True,
        invoke_self_block_update=True,
        show_on_client=True,
    ):
        raise NotImplementedError

    async def remove_block(
        self,
        position: BLOCK_POSITION,
        invoke_block_updates=True,
        invoke_self_block_update=True,
    ):
        raise NotImplementedError

    async def get_block(self, position: BLOCK_POSITION):
        raise NotImplementedError

    async def get_block_type(self, position: BLOCK_POSITION) -> str:
        return (await self.get_block(position)).NAME

    async def invoke_block_update_around(self, position: BLOCK_POSITION):
        raise NotImplementedError


class AbstractChunk(AbstractBlockAccess, ABC):
    def get_position(self) -> CHUNK_POSITION:
        raise NotImplementedError

    def get_dimension(self) -> "AbstractDimension":
        raise NotImplementedError

    async def save(self):
        pass

    async def load(self):
        pass

    def is_loaded(self) -> bool:
        raise NotImplementedError

    def is_generated(self) -> bool:
        raise NotImplementedError

    async def generate(self):
        raise NotImplementedError

    async def add_force_load_ticket(self, source: str):
        raise NotImplementedError

    async def remove_force_load_ticket(self, source: str):
        raise NotImplementedError

    async def is_chunk_force_loaded(self, by: str = None) -> bool:
        raise NotImplementedError

    async def enforce_no_force_load(self):
        raise NotImplementedError

    async def force_block_redraw(self, position: BLOCK_POSITION):
        raise NotImplementedError


class AbstractDimension(AbstractBlockAccess, ABC):
    async def save(self):
        pass

    async def load(self):
        pass

    def get_world(self) -> "AbstractWorld":
        raise NotImplementedError

    async def get_chunk(self, position: CHUNK_POSITION) -> AbstractChunk:
        raise NotImplementedError

    async def get_chunk_for_position(self, position: BLOCK_POSITION) -> AbstractChunk:
        raise NotImplementedError

    async def remove_all_force_loads(self):
        raise NotImplementedError

    def chunk_iterator(self) -> typing.Iterable[AbstractChunk]:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_valid_height_range(self) -> typing.Tuple[int, int]:
        return 0, 255

    async def generate_chunk(self, position: CHUNK_POSITION):
        pass


class AbstractWorld(ABC):
    async def save(self):
        pass

    async def load(self):
        pass

    async def get_dimension(self, name: str) -> AbstractDimension:
        raise NotImplementedError

    async def add_dimension(self, name: str) -> AbstractDimension:
        raise NotImplementedError
