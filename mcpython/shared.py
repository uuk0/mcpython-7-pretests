import typing
import os

import asyncm.Manager as _Manager

async_side_instance: typing.Optional[_Manager.SpawnedProcessInfo] = None


local = os.path.dirname(os.path.dirname(__file__))

resource_manager = None
