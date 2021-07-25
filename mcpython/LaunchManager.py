import asyncm.Manager
import asyncm.pyglet_binding


async def spawn_window(side: asyncm.Manager.SpawnedProcessInfo):
    window = await side.pyglet_manager.spawn_custom_window("mcpython.client.rendering.Window", "Window")


class LaunchManager:
    def __init__(self):
        self.async_manager = asyncm.Manager.AsyncProcessManager()
        asyncm.pyglet_binding.spawn_in(self.async_manager)

    def launch(self):
        self.async_manager.add_process("world")
        self.async_manager.add_process("world_generation")
        self.async_manager.add_process("network")
        self.async_manager.add_process("data_processing")

        self.async_manager.run_regular_on_process("pyglet", spawn_window)

        self.async_manager.main()

