from mcpython.common.event.EventCycle import EventDispatcher


INIT = EventDispatcher("minecraft:init")

WINDOW_CREATION = EventDispatcher("minecraft:window_creation")

EXIT = EventDispatcher("minecraft:exit")
CRASH = EventDispatcher("minecraft:crash")
