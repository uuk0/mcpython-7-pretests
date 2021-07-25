import asyncio
import typing

import asyncm.Manager


class PygletDataManager:
    """
    Binding manager for a pyglet backend with support for async stuff handling
    """

    def __init__(self, side: asyncm.Manager.SpawnedProcessInfo):
        self.side = side
        self.windows = []
        self.window_spawn_in_progress = False

        import pyglet

        self.temp_win: typing.Optional[pyglet.window.Window] = pyglet.window.Window(caption="Temporary Window")

        self.event_loop = pyglet.app.event_loop
        self.platform_event_loop = pyglet.app.platform_event_loop

    async def setup(self):
        import pyglet
        self.event_loop.clock.schedule_interval_soft(self.event_loop._redraw_windows, 1/60)  # these are the MAX FPS
        self.event_loop.has_exit = False

        from pyglet.window import Window
        Window._enable_event_queue = False

        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_pending_events()

        self.platform_event_loop.start()

        self.event_loop.dispatch_event("on_enter")
        self.event_loop.is_running = True

        self.side.call_regular = self.step

    async def spawn_default_window(
        self, *args, invoke_with_window=None, on_draw_callback=None, **kwargs
    ):
        self.window_spawn_in_progress = True

        import pyglet

        win = pyglet.window.Window(*args, **kwargs)

        @win.event
        def on_close():
            async def close(side):
                side.sided_task_manager.main_obj.stop()

            self.side.sided_task_manager.invokeOnMainNoWait(close)

        @win.event
        def on_draw():
            pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
            win.clear()

            if on_draw_callback is not None:
                on_draw_callback(win)

        await self._setup_win(win, invoke_with_window=invoke_with_window)

        self.window_spawn_in_progress = False

        return win

    async def spawn_custom_window(
        self, win_module: str, win_attr: str, *args, invoke_with_window=None, **kwargs
    ):
        self.window_spawn_in_progress = True

        import importlib

        module = importlib.import_module(win_module)
        win_class = getattr(module, win_attr)

        win = win_class(self.side, *args, **kwargs)
        await self._setup_win(win, invoke_with_window=invoke_with_window)

        self.window_spawn_in_progress = False

        return win

    async def _setup_win(self, win, invoke_with_window=None):
        win.async_manager = self

        self.windows.append(win)

        if invoke_with_window is not None:
            await invoke_with_window(self, win)

    async def step(self, _):
        if self.window_spawn_in_progress: return

        if self.temp_win is not None:
            self.temp_win.close()
            self.temp_win = None

        # todo: can we do some stuff async?
        timeout = self.event_loop.idle()
        self.platform_event_loop.step(timeout)

    async def check_exit(self):
        if self.event_loop.has_exit:
            self.event_loop.is_running = False
            self.event_loop.dispatch_event("on_exit")
            self.platform_event_loop.stop()

            asyncio.get_running_loop().stop()


def spawn_in(process_manager: asyncm.Manager.AsyncProcessManager):
    process_manager.add_process("pyglet")

    async def spawn(side: asyncm.Manager.SpawnedProcessInfo):
        print("spawning pyglet side")
        import pyglet

        # This is needed as the code is not executed in the same context
        from asyncm.pyglet_binding import PygletDataManager

        side.pyglet_manager = PygletDataManager(side)
        await side.pyglet_manager.setup()

    process_manager.run_regular_on_process("pyglet", spawn)
