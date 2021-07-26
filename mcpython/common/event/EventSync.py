import asyncio
import time
import typing
from abc import ABC

import asyncm.Manager
import mcpython.shared
from mcpython import shared


class Event(ABC):
    __slots__ = ("creation_time",)

    NAME: str = None
    BUS: str = None

    def __init__(self):
        self.creation_time = time.time()


class EventListener(ABC):
    @classmethod
    async def invokeListener(
        cls,
        event: Event,
        listener: typing.Union[
            "EventListener", typing.Callable[[Event], typing.Awaitable]
        ],
    ):
        if isinstance(listener, EventListener):
            return await listener.invoke(event)
        return await listener(event)

    async def invoke(self, event: Event):
        raise NotImplementedError


class ProcessLinkingEventListener(EventListener):
    def __init__(
        self,
        process: str,
        listener: typing.Union[
            EventListener, typing.Callable[[Event], typing.Awaitable]
        ],
    ):
        self.process = process
        self.listener = listener

    async def invoke(self, event: Event):
        mcpython.shared.async_side_instance.sided_task_manager.invokeOnNoWait(
            self.process, self.invokeInternal, event
        )

    async def invokeInternal(self, event: Event):
        await self.invokeListener(event, self.listener)


def registerEventListener(
    event_type: typing.Union[str, typing.Type[Event]],
    listener: typing.Union[EventListener, typing.Callable[[Event], typing.Awaitable]],
):
    """
    Registers a callback for an event
    The listener will be invoked on the event_router process
    :param event_type: the type to listen for, either the name of the event or the event class
    :param listener: the listener, either an instance of EventListener or a callable-await-able
    """
    shared.async_side_instance.sided_task_manager.invokeOnNoWait(
        "event_router", internalRegisterEventListener, event_type, listener
    )


async def internalRegisterEventListener(
    side: asyncm.Manager.SpawnedProcessInfo,
    event_type: typing.Union[str, typing.Type[Event]],
    listener: typing.Union[EventListener, typing.Callable[[Event], typing.Awaitable]],
):
    import mcpython.common.event.EventSync

    mcpython.common.event.EventSync.EventManager.INSTANCE.registerListener(
        event_type, listener
    )


def registerProcessBoundEventListener(
    event_type: typing.Union[str, typing.Type[Event]],
    listener: typing.Union[EventListener, typing.Callable[[Event], typing.Awaitable]],
    process: str = None,
):
    """
    Registers a callback for an event
    The listener will be invoked on the process (defaults to this process)
    :param event_type: the type to listen for, either the name of the event or the event class
    :param listener: the listener, either an instance of EventListener or a callable-await-able
    :param process: the process to invoke on
    """
    if process is None:
        process = mcpython.shared.async_side_instance.name

    registerEventListener(event_type, ProcessLinkingEventListener(process, listener))


class EventManager:
    # On event_router, this is the instance of it
    INSTANCE: typing.Optional["EventManager"] = None

    def __init__(self):
        self.event_types: typing.Dict[str, typing.Type[Event]] = {}
        self.bus2event2listeners: typing.Dict[
            str,
            typing.Dict[
                str,
                typing.List[
                    typing.Union[
                        EventListener, typing.Callable[[Event], typing.Awaitable]
                    ]
                ],
            ],
        ] = {}

    def registerListener(
        self,
        event_type: typing.Union[str, typing.Type[Event]],
        listener: typing.Union[
            EventListener, typing.Callable[[Event], typing.Awaitable]
        ],
    ):
        if isinstance(event_type, str):
            event_type = self.event_types[event_type]
        self.bus2event2listeners.setdefault(event_type.BUS, {}).setdefault(
            event_type.NAME, []
        ).append(listener)

    async def invokeEvent(self, event: Event):
        listeners = self.bus2event2listeners.setdefault(event.BUS, {}).setdefault(
            event.NAME, []
        )
        await asyncio.gather(
            *(EventListener.invokeListener(event, listener) for listener in listeners)
        )


async def setup_event_router(side: asyncm.Manager.SpawnedProcessInfo):
    import mcpython.common.event.EventSync

    mcpython.common.event.EventSync.EventManager.INSTANCE = (
        side.event_manager
    ) = mcpython.common.event.EventSync.EventManager()


def invokeEventFromOutside(event: Event):
    shared.async_side_instance.sided_task_manager.invokeOnNoWait(
        "event_router", internalInvokeEvent, event
    )


async def internalInvokeEvent(_, event: Event):
    import mcpython.common.event.EventSync

    await mcpython.common.event.EventSync.EventManager.INSTANCE.invokeEvent(event)
