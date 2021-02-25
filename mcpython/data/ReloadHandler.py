import mcpython.data.codec.AbstractCodec
import enum
from mcpython import shared


class ReloadPhase(enum.Enum):
    """ "
    Reload phase enum
    Called in the order listed
    """

    PRE = 0
    DATA = 1
    POST = 2


class ReloadHandler:
    """
    Handler for reloading assets and data from the resource locations specified in advance by their Codec
    """

    def __init__(self):
        pass

    def register_reload_codec(
        self,
        base_file: str,
        codec: mcpython.data.codec.AbstractCodec.AbstractCodec,
        target_invoke,
        target_process: str = "file_io",
    ):
        """
        Registers a reload listener, loading data on each reload
        :param base_file: the base file, example: 'assets/{namespace}/textures/block' will load all files in
            assets/{namespace}/textures/block
        :param codec: the codec to use for decoding
        :param target_invoke: what to invoke, encode-able by the process manager system
            (Signature: (Handler, Decoded Object)
        :param target_process: the target process to invoke on
        """

    def register_reload_callback(
        self, target, target_process: str = "file_io", phase=ReloadPhase.DATA
    ):
        """
        Registers a reload callback
        :param target: the target
        :param target_process: the target process to invoke on
        :param phase: the phase to invoke in, see ReloadPhase-enum for things
        """

    def reload(self):
        pass


shared.reload_handler = ReloadHandler()
