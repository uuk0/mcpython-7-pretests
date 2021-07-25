import pyglet
import asyncm.Manager


class Window(pyglet.window.Window):
    def __init__(self, side: asyncm.Manager.SpawnedProcessInfo):
        super().__init__(resizable=True, caption="mcpython 7 pretests - Iteration II")
        self.side = side

    def on_draw(self):
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self.clear()

    def on_close(self):
        self.side.sided_task_manager.close()

