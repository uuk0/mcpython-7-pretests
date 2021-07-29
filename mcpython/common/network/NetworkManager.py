import typing

from mcpython import shared
from mcpython.common.network.package.AbstractPackage import AbstractPackage, DefaultPackage


class NetworkManager:
    PACKAGE_TYPES: typing.Dict[bytes, typing.Type[AbstractPackage]] = {}

    def __init__(self):
        self.side_manager = None
        self.is_client = None

        self.package_handlers: typing.Dict[bytes, typing.Callable] = {}

    def spawn_client_network_instance(self):
        import mcpython.common.network.NetworkBuilder

        self.side_manager = mcpython.common.network.NetworkBuilder.RemoteNetworkConnector()
        self.is_client = True

        shared.async_side_instance.call_regular = self.handle_client

    def spawn_server_network_instance(self):
        import mcpython.common.network.NetworkBuilder

        self.side_manager = (
            mcpython.common.network.NetworkBuilder.NetworkBuilder()
        )
        self.is_client = False

        shared.async_side_instance.call_regular = self.handle_server

    def disconnect(self):
        if self.side_manager is not None:
            self.side_manager.disconnect()
        self.is_client = None
        shared.async_side_instance.call_regular = None

    def send(self, package: AbstractPackage, target: int = -1):
        if self.is_client is True:
            self.side_manager.send_queue.append(package.serialize())
        elif self.is_client is False:
            self.side_manager.connected_clients[target].send(package.serialize())
        else:
            raise RuntimeError("network not set up correctly!")

    async def handle_client(self):
        self.side_manager.handle()

        for head, size, body in self.side_manager.receive_queue:
            package_type = self.PACKAGE_TYPES[head]
            package = package_type.deserialize(body)

            if head in self.package_handlers:
                await self.package_handlers[head](package)

    async def handle_server(self):
        for client in self.side_manager.connected_clients:
            while len(client.receive_queue):
                head, size, body = client.receive_queue.pop()
                package_type = self.PACKAGE_TYPES[head]
                package = package_type.deserialize(body)

                if head in self.package_handlers:
                    await self.package_handlers[head](client, package)


async def setup(side):
    from mcpython.common.network.NetworkManager import NetworkManager

    shared.network_manager = NetworkManager()
