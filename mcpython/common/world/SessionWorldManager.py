import mcpython.common.world.abstract
from mcpython import shared


class SessionWorldManager:
    def __init__(self):
        self.current_world = None

    def create_new_local_world(self) -> mcpython.common.world.abstract.AbstractWorld:
        import mcpython.common.world.IntegratedWorldImplementation

        world = mcpython.common.world.IntegratedWorldImplementation.IntegratedWorld()

        self.join_world(world)

        return world

    def join_world(self, world: mcpython.common.world.abstract.AbstractWorld):
        shared.world = world

    def leave_world(self):
        pass

    def prepare_world_from_remote(self):
        pass


async def setup_session_manager(side):
    from mcpython import shared
    from mcpython.common.world.SessionWorldManager import SessionWorldManager

    import mcpython.server.worldgen.WorldGenerationHandler

    shared.world_session_manager = SessionWorldManager()
    shared.world_generation_manager = (
        mcpython.server.worldgen.WorldGenerationHandler.WorldGenerationHandler()
    )

    world = shared.world_session_manager.create_new_local_world()
    dimension = await world.add_dimension("overworld")

    dimension.chunk_generator = shared.world_generation_manager.new_chunk_generator(
        "default"
    )

    await dimension.generate_chunk((0, 0))
    await dimension.add_block((0, 0, 0), "minecraft:stone")
