

def rendering(handler):
    import pyglet
    import mcpython.rendering.Window

    window = mcpython.rendering.Window.Window()
    handler.window = window

    pyglet.clock.schedule_interval(handler.fetch, 0.3)
    pyglet.app.run()

    handler.stop()


class LaunchWrapper:
    def __init__(self):
        pass

    def setup(self):
        import mcpython.ProcessManager
        mcpython.ProcessManager.spawn_process("rendering", target=rendering)
        mcpython.ProcessManager.spawn_process("world_handling")
        mcpython.ProcessManager.spawn_process("world_generation")
        mcpython.ProcessManager.spawn_process("network")

        """
        How split on processes?
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

    def launch(self):
        import mcpython.ProcessManager

        # This are tests for testing cross-process task sending
        # mcpython.ProcessManager.execute_on("rendering", lambda handler: print("Hello World!"))
        # mcpython.ProcessManager.execute_on("world_handling", lambda handler: handler.execute_on("main", lambda: print("Back!")))
        # mcpython.ProcessManager.execute_on("world_handling", lambda handler: handler.execute_on("network", lambda h: print("Cross!")))

        mcpython.ProcessManager.start_processes()
        mcpython.ProcessManager.maintain()

