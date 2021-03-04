import time


def rendering(handler):
    """
    Main loop for rendering system
    Hands the fetch() call over to the pyglet clock, ticking each 1/20s

    todo: setup OpenGL
    todo: setup rendering Pipe
    """
    import pyglet
    import mcpython.rendering.Window

    window = mcpython.rendering.Window.Window(handler)
    handler.window = window

    pyglet.clock.schedule_interval(handler.fetch, 0.3)
    pyglet.app.run()

    handler.stop()


class LaunchWrapper:
    # todo: share this when there is more config here...

    def __init__(self):
        pass

    def setup(self):
        import mcpython.ProcessManager

        mcpython.ProcessManager.setup_dict()

        mcpython.ProcessManager.spawn_process("file_io")
        mcpython.ProcessManager.spawn_process("rendering", target=rendering)
        mcpython.ProcessManager.spawn_process("world_handling")
        mcpython.ProcessManager.spawn_process("world_generation", async_process=True)
        mcpython.ProcessManager.spawn_process("network", async_process=True)

        """
        How split on processes?
        - file_io: process for accessing data and handling it, only process for accessing ResourceLocator
            todo: reload system goes here
        - rendering is driven by pyglet main thread and fetches events from pyglet, and requests for changing
            whats rendered, calculating stuff off-thread and re-injecting it into the default task pipe if needed
        - world_handling stores the whole world, for every dimension having its own thread (as long as there are
            not too much dimensions, otherwise, there should be some clever merging), and ticking happening in each
            thread
        - world_generation handles world generation, with multiple threads.
            It contains local Chunk instances later send to the world handling thread for processing.
            It uses a async system under the hood, so waiting for chunk info of other chunks to arrive
            is not loosing time
        - network is network handling, nothing more to say. Is allowed to send requests to other processes,
            may use also async for handling and waiting for stuff
        """

        # Setup resource system
        mcpython.ProcessManager.execute_on(
            "file_io",
            """
import mcpython.data.ResourceLocator
import mcpython.shared
mcpython.shared.get_resource_locator().load_default_resources()
handler.set_flag('resource_locator:load_complete')""",
        )

    def launch(self):
        import mcpython.ProcessManager

        mcpython.ProcessManager.start_processes()
        mcpython.ProcessManager.maintain()

    def run_data_gen(self):
        import mcpython.data.gen.Driver

        mcpython.data.gen.Driver.work_vanilla()
