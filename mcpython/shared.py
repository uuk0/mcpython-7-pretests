import tempfile
import os

local = os.path.dirname(os.path.dirname(__file__))


class MC:
    MC_BASE_NAME = "21w08a"
    ASSET_SOURCE_URL = "https://launcher.mojang.com/v1/objects/3a008c012bd6bba29054701c7797493523660c57/client.jar"


tmp = tempfile.TemporaryDirectory()

resource_locator = None


def get_resource_locator():
    if resource_locator is None:
        raise ValueError("wrong process!")

    return resource_locator
