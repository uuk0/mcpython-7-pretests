import pyglet


class Window(pyglet.window.Window):
    """
    Base class for the pyglet connection system
    todo: share events over event-bus
    todo: add COM for setting properties from other Processes
    todo: add key & mouse logger for lookup
    todo: on each tick, do stuff
    """

    def __init__(self, process_handler):
        super().__init__(resizable=True, caption="Mcpython 7 pre-tests")
        self.process_handler = process_handler

        pyglet.clock.schedule_interval(self.tick, 0.05)

    def on_draw(self):
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self.clear()

    def tick(self, dt: float):
        if not self.process_handler.running:
            self.close()
