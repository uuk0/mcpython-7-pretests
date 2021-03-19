import enum


class NetworkSide(enum.Enum):
    # Used on client internal communications
    # Used only in a few places, were there is a "both" state
    CLIENT_SERVER = True, True

    # Can be used for external software to indicate that it is None of the other ones
    # May also be set when not in world as an indicator for "do nothing"
    NONE = False, False

    # This are the "normal" sides
    CLIENT_DEDICATED = True, False
    SERVER_DEDICATED = False, True

    def __init__(self, is_client: bool, is_server: bool):
        self.is_client = is_client
        self.is_server = is_server

    def __hash__(self):
        return hash(self.is_client) * 10 + hash(self.is_server)

    def __eq__(self, other):
        return isinstance(other, NetworkSide) and self.is_client == other.is_client and self.is_server == other.is_server

