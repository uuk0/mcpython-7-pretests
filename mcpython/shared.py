import typing
import os

import asyncm.Manager as _Manager

import mcpython.common.world.abstract

async_side_instance: typing.Optional[_Manager.SpawnedProcessInfo] = None


local = os.path.dirname(os.path.dirname(__file__))

resource_manager = None
network_manager = None

is_client = None

world_session_manager = None
world_generation_manager = None
world: typing.Optional[mcpython.common.world.abstract.AbstractWorld] = None
