import marshal
import types


GLOBAL = globals()
GLOBAL_INITED = False


def init_global():
    global GLOBAL_INITED

    if not GLOBAL_INITED:
        return

    exec(
        """
    import time, os, asyncio
    from mcpython import shared
    """,
        GLOBAL,
    )
    GLOBAL_INITED = True


def serialize_task(function, args, kwargs, meta=None):
    return marshal.dumps(function.__code__), args, kwargs, meta


def deserialize_task(data):
    init_global()
    return (types.FunctionType(marshal.loads(data[0]), GLOBAL),) + data[1:]
