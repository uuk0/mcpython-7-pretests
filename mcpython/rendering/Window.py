import pyglet


class Window(pyglet.window.Window):
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
