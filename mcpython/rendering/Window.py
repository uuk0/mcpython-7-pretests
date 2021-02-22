import pyglet


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(resizable=True, caption="Mcpython 7 pre-tests")

    def on_draw(self):
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self.clear()
