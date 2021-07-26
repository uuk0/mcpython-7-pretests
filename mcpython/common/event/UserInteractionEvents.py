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
