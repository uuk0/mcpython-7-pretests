import asyncm.Manager
import asyncm.pyglet_binding


async def spawn_window(side: asyncm.Manager.SpawnedProcessInfo):
    window = await side.pyglet_manager.spawn_custom_window(
        "mcpython.client.rendering.Window", "Window"
    )

    # import mcpython.client.texture.TextureAtlas
    # atlas = mcpython.client.texture.TextureAtlas.TextureAtlas()
    # await atlas.async_add_texture("assets/minecraft/textures/block/stone.png")
    # await atlas.async_add_texture("assets/minecraft/textures/block/oak_planks.png")
    # await atlas.async_add_texture("assets/minecraft/textures/block/bedrock.png")
    # atlas.bake()


class LaunchManager:
    def __init__(self):
        self.async_manager = asyncm.Manager.AsyncProcessManager()

    def launch(self):
        # the system for rendering
        asyncm.pyglet_binding.spawn_in(self.async_manager)
        self.async_manager.run_regular_on_process("pyglet", spawn_window)

        # the process storing the world and its information
        self.async_manager.add_process("world")

        # the process for world generation
        self.async_manager.add_process("world_generation")

        # the process handling networking
        self.async_manager.add_process("network")

        import mcpython.common.network.NetworkManager

        self.async_manager.run_regular_on_process(
            "network", mcpython.common.network.NetworkManager.setup
        )

        # A general data processing & preparation process
        # Contains the system to read/write files
        self.async_manager.add_process("data_processing")

        import mcpython.ResourceLocator

        self.async_manager.run_regular_on_process(
            "data_processing", mcpython.ResourceLocator.setup_side
        )

        # a process which gets all the events from the backend & system and handles them
        self.async_manager.add_process("event_router")

        import mcpython.common.event.EventSync

        self.async_manager.run_regular_on_process(
            "event_router", mcpython.common.event.EventSync.setup_event_router
        )

        self.async_manager.main()
