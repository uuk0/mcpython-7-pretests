import typing


class EventDispatcher:
    """
    Class for a caller of a event
    Holds some information about the event, and makes faster calls possible [no slow event target lookups needed]
    todo: add some form of check or wrapper for process target
    """

    def __init__(
        self,
        event_name: str,
        expected_signature: typing.Optional[
            typing.Tuple[typing.Tuple[typing.Type], typing.Dict[str, typing.Type]]
        ] = None,
    ):
        self.event_name = event_name
        self.expected_signature = expected_signature

        self.subscribers: typing.List["EventAnnotator"] = []

    def call(self, *args, **kwargs):
        """
        Calls the event over all subscribed annotators
        """
        for sub in self.subscribers:
            sub.invoke(*args, **kwargs)

    def call_yield_results(self, *args, **kwargs):
        """
        Same as call, but will yield all results of function calls
        """
        for sub in self.subscribers:
            yield sub.invoke(*args, **kwargs)

    def call_cancelable(self, *args, **kwargs) -> bool:
        """
        Same as call, but when a function returns bool(...)->True, it will exit and return the value, otherwise False
        """
        for sub in self.subscribers:
            canceled = sub.invoke(*args, **kwargs)
            if canceled:
                return canceled

        return False


class EventAnnotator:
    """
    Class for subscribing to a event
    """

    def __init__(self, info=None):
        self.info = info
        self.dispatcher: typing.Optional[EventDispatcher] = None
        self.target = None

    def link_to_dispatcher(self, dispatcher: EventDispatcher):
        self.dispatcher = dispatcher
        dispatcher.subscribers.append(self)

    def __call__(self, func):
        self.target = func
        return func

    def invoke(self, *args, **kwargs) -> typing.Optional[typing.Any]:
        pass
