"""
Shared.py contains data shared in the same process
local is the main path

resource_locator is optional the ResourceLocator instance, use get_resource_locator() for safe access

tmp is the temporary folder for this process

MC contains constants around the mc version this is based on
"""

import tempfile
import os

local = os.path.dirname(os.path.dirname(__file__))


VERSION_NAME = "BUILD 38"


class MC:
    MC_BASE_NAME = "21w08a"
    ASSET_SOURCE_URL = "https://launcher.mojang.com/v1/objects/3a008c012bd6bba29054701c7797493523660c57/client.jar"


tmp = tempfile.TemporaryDirectory()

# not-main only
process_handler = None

# file_io only
resource_locator = None
reload_handler = None

# World handling only
world = None

block_registry = None
block_plugin_registry = None


def get_resource_locator():
    if resource_locator is None:
        raise ValueError("wrong process!")

    return resource_locator
