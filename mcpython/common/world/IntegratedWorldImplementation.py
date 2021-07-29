"""
The implementation for local worlds

Uses IntegratedServerNetworkAdapter when opeing to LAN
"""

import typing

import mcpython.common.world.abstract
from mcpython.common.world.abstract import AbstractChunk
from mcpython.common.world.abstract import AbstractDimension
from mcpython.common.world.abstract import BLOCK_POSITION
from mcpython.common.world.abstract import CHUNK_POSITION

import mcpython.util.math
import collections


class IntegratedChunk(mcpython.common.world.abstract.AbstractChunk):
    def __init__(self, dimension: "IntegratedDimension", position: CHUNK_POSITION):
        self.dimension = dimension
        self.position = position

        self.loaded = True
        self.force_load_tickets = set()

        self.world = {}

    def get_position(self) -> CHUNK_POSITION:
        return self.position

    def get_dimension(self) -> "AbstractDimension":
        return self.dimension

    def is_loaded(self) -> bool:
        return self.loaded

    async def add_force_load_ticket(self, source: str):
        self.force_load_tickets.add(source)

    async def remove_force_load_ticket(self, source: str):
        self.force_load_tickets.remove(source)

    async def is_chunk_force_loaded(self, by: str = None) -> bool:
        return (by in self.force_load_tickets) if by is not None else (len(self.force_load_tickets) > 0)

    async def enforce_no_force_load(self):
        self.force_load_tickets.clear()

    async def add_block(
        self,
        block_type,
        position: BLOCK_POSITION,
        meta=None,
        invoke_block_updates=True,
        invoke_self_block_update=True,
        show_on_client=True,
    ):
        pass

    async def remove_block(
        self,
        position: BLOCK_POSITION,
        invoke_block_updates=True,
        invoke_self_block_update=True,
    ):
        block = self.world.pop(position, None)

        if block is None: return

    async def get_block(self, position: BLOCK_POSITION):
        return self.world.get(position, None)

    async def invoke_block_update_around(self, position: BLOCK_POSITION):
        pass

    async def force_block_redraw(self, position: BLOCK_POSITION):
        pass


class IntegratedDimension(mcpython.common.world.abstract.AbstractDimension):
    def __init__(self, name: str, world: "IntegratedWorld"):
        self.world = world
        self.name = name
        self.chunks: typing.Dict[CHUNK_POSITION, IntegratedChunk] = {}

    def get_world(self) -> "IntegratedWorld":
        return self.world

    async def get_chunk(self, position: CHUNK_POSITION) -> AbstractChunk:
        if position not in self.chunks:
            self.chunks[position] = IntegratedChunk(self, position)
        return self.chunks[position]

    async def get_chunk_for_position(self, position: BLOCK_POSITION) -> AbstractChunk:
        return await self.get_chunk(mcpython.util.math.position2chunk(position))

    async def remove_all_force_loads(self):
        for chunk in self.chunks.values():
            await chunk.enforce_no_force_load()

    def chunk_iterator(self) -> typing.Iterable[AbstractChunk]:
        return iter(self.chunks.values())

    def get_name(self) -> str:
        return self.name

    async def add_block(
        self,
        block_type,
        position: BLOCK_POSITION,
        meta=None,
        invoke_block_updates=True,
        invoke_self_block_update=True,
        show_on_client=True,
    ):
        return await (await self.get_chunk_for_position(position)).add_block(block_type, position, meta, invoke_block_updates, invoke_self_block_update, show_on_client)

    async def remove_block(
        self,
        position: BLOCK_POSITION,
        invoke_block_updates=True,
        invoke_self_block_update=True,
    ):
        return await (await self.get_chunk_for_position(position)).remove_block(position, invoke_block_updates, invoke_self_block_update)

    async def get_block(self, position: BLOCK_POSITION):
        return await (await self.get_chunk_for_position(position)).get_block(position)

    async def invoke_block_update_around(self, position: BLOCK_POSITION):
        await (await self.get_chunk_for_position(position)).invoke_block_update_around(position)


class IntegratedWorld(mcpython.common.world.abstract.AbstractWorld):
    def __init__(self):
        self.dimensions: typing.Dict[str, IntegratedDimension] = {}

    async def get_dimension(self, name: str) -> AbstractDimension:
        return self.dimensions.get(name, None)
