import time
import typing

import pyglet
import asyncm.Manager
import mcpython.common.event.EventSync as EventSync
import mcpython.common.event.UserInteractionEvents as Events


class Window(pyglet.window.Window):
    def __init__(self, side: asyncm.Manager.SpawnedProcessInfo):
        super().__init__(resizable=True, caption="mcpython 7 pretests - Iteration II")
        self.side = side

        self.key_press_timers: typing.Dict[int, float] = {}
        self.mouse_press_timers: typing.Dict[int, float] = {}

    def on_draw(self):
        pyglet.gl.glClearColor(255, 255, 255, 255)
        self.clear()

    def on_close(self):
        self.side.sided_task_manager.close()

    def on_key_press(self, symbol, modifiers):
        event = Events.UserKeyStateChangeEvent(symbol, modifiers, True)
        EventSync.invokeEventFromOutside(event)
        self.key_press_timers[symbol] = time.time()

    def on_key_release(self, symbol, modifiers):
        event = Events.UserKeyStateChangeEvent(
            symbol,
            modifiers,
            False,
            time.time() - self.key_press_timers.pop(symbol, time.time()),
        )
        EventSync.invokeEventFromOutside(event)

    def on_mouse_press(self, x, y, button, modifiers):
        event = Events.MousePressStateChangeEvent((x, y), button, modifiers, True)
        EventSync.invokeEventFromOutside(event)

    def on_mouse_release(self, x, y, button, modifiers):
        event = Events.MousePressStateChangeEvent(
            (x, y),
            button,
            modifiers,
            False,
            time.time() - self.mouse_press_timers.pop(button, time.time()),
        )
        EventSync.invokeEventFromOutside(event)

    def on_mouse_motion(self, x, y, dx, dy):
        event = Events.MouseMotionEvent(x, y, dx, dy)
        EventSync.invokeEventFromOutside(event)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        event = Events.MouseMotionEvent(x, y, dx, dy, buttons, modifiers)
        EventSync.invokeEventFromOutside(event)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        event = Events.MouseWheelScrollEvent((x, y), scroll_x + scroll_y)
        EventSync.invokeEventFromOutside(event)

    def on_resize(self, width, height):
        event = Events.WindowResizeEvent(width, height)
        EventSync.invokeEventFromOutside(event)

    def on_context_lost(self):
        for button in self.mouse_press_timers.keys():
            self.on_mouse_release(0, 0, button, 0)
        self.mouse_press_timers.clear()
        for key in self.key_press_timers.keys():
            self.on_key_release(key, 0)
        self.key_press_timers.clear()
