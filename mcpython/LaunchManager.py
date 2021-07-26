import asyncm.Manager
import asyncm.pyglet_binding


async def spawn_window(side: asyncm.Manager.SpawnedProcessInfo):
    window = await side.pyglet_manager.spawn_custom_window(
        "mcpython.client.rendering.Window", "Window"
    )


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

        # a general data processing & preparation process
        self.async_manager.add_process("data_processing")

        # a process which gets all the events from the backend & system and handles them
        self.async_manager.add_process("event_router")

        import mcpython.common.event.EventSync

        self.async_manager.run_regular_on_process(
            "event_router", mcpython.common.event.EventSync.setup_event_router
        )

        self.async_manager.main()
