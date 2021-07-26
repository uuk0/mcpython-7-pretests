import typing

from mcpython.common.event.EventSync import Event


class UserKeyStateChangeEvent(Event):
    """
    An event indicating a key press / release by the user

    press_time may be the time the key was pressed, may not be present
    """

    BUS = "minecraft:user_interaction"
    NAME = "minecraft:key_state_change"

    __slots__ = ("key", "mods", "state", "press_time")

    def __init__(self, key: int, mods: int, state: bool, press_time: float = None):
        super().__init__()
        self.key = key
        self.mods = mods
        self.state = state
        self.press_time = press_time


class MousePressStateChangeEvent(Event):
    """
    An event indicating a mouse button press / release by the user

    press_time may be the time the key was pressed, may not be present
    """

    BUS = "minecraft:user_interaction"
    NAME = "minecraft:mouse_state_change"

    __slots__ = ("position", "button", "mods", "state", "press_time")

    def __init__(
        self,
        position: typing.Tuple[int, int],
        button: int,
        mods: int,
        state: bool,
        press_time: float = None,
    ):
        super().__init__()
        self.position = position
        self.button = button
        self.mods = mods
        self.state = state
        self.press_time = press_time


class MouseMotionEvent(Event):
    BUS = "minecraft:user_interaction"
    NAME = "minecraft:mouse_motion"

    __slots__ = ("x", "y", "dx", "dy", "button", "mods")

    def __init__(self, x: int, y: int, dx: int, dy: int, button: int = 0, mods: int = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.button = button
        self.mods = mods


class MouseWheelScrollEvent(Event):
    BUS = "minecraft:user_interaction"
    NAME = "minecraft:mouse_wheel_scroll"

    __slots__ = ("position", "amount")

    def __init__(self, position: typing.Tuple[int, int], amount: int):
        super().__init__()
        self.position = position
        self.amount = amount


class WindowResizeEvent(Event):
    BUS = "minecraft:user_interaction"
    NAME = "minecraft:window_resize"

    __slots__ = ("wx", "wy")

    def __init__(self, wx: int, wy: int):
        super().__init__()
        self.wx = wx
        self.wy = wy
