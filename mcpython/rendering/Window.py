import pyglet
from mcpython import shared


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

        self.label_batch = pyglet.graphics.Batch()

        self.version_info_label = pyglet.text.Label(text=f"MCPYTHON PRE-ALPHA "+shared.VERSION_NAME, color=(0, 0, 0, 255), batch=self.label_batch)
        self.fps_label = pyglet.text.Label(text="fps: -", color=(0, 0, 0, 255), batch=self.label_batch)

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.version_info_label.y = self.get_size()[1] - self.version_info_label.content_height - 10
        self.fps_label.text = "fps: "+str(pyglet.clock.get_fps())
        self.fps_label.y = self.get_size()[1] - self.version_info_label.content_height - self.fps_label.content_height - 20
        self.label_batch.draw()

    def tick(self, dt: float):
        if not self.process_handler.running:
            self.close()
