import abc
import mcpython.common.event.Registry


class BlockPlugin(mcpython.common.event.Registry.IRegistryContent, abc.ABC):
    pass
