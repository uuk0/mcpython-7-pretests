"""
Mcpython network protocoll
<2B: network bus><2B: package type><1-16B (depending on package type) package size><package content>

Bus 0x0000: foundation bus
    0x0000: client -> server status ping
    0x0001: server -> client status ping response
    0x0002: server -> client handshake error (at any point)
    0x0003: client -> server connection request
    0x0004: server -> client connection request result
        2B size, 1B request answer [general]
            00: InternalServerError [Unhandled internal error]
            01: ServerClosedError [Server is not able as it is shut down / shutting down]
            02: PlayerBannedError -> 1B String reason  [Player was banned by player name]
            03: PlayerIPBannedError -> 1B String reason  [Player was banned by player IP]
            04: ServerIsFulError -> 2B max players  [No more room on this server]
            05: PlayerDataDecodingError  [Internal error during loading player data from saves]
            06: ConnectionSuccessful
    0x0005: re-rout package (client -> server)
        16B size, 2B target, followed by a default package

"""

import socket
import threading
import typing
import collections


class ConnectedClient:
    def __init__(self):
        self.connection_object = None

        self.send_queue = collections.deque()
        self.receive_queue = collections.deque()

        self.client_id = -1


class NetworkBuilder:
    """
    The network manager at the server
    """

    def __init__(self):
        self.handler_threads = []
        self.connected_clients = []

        self.head2size_size = {}

    def server_main(self):
        # get the hostname
        host = socket.gethostname()
        port = 5000  # initiate port no above 1024

        server_socket = socket.socket()  # get instance
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        # todo: move to server config
        server_socket.listen(2)

        while True:
            # accept new connection
            pair = server_socket.accept()

            client = ConnectedClient()
            client.client_id = len(self.connected_clients)

            self.connected_clients.append(client)

            thread = threading.Thread(target=self.work_connection, args=(pair, client))
            thread.start()
            self.handler_threads.append(thread)

    def work_connection(self, pair, client):
        conn, address = pair

        client.connection_object = conn

        conn.send(b"\x00\x00\x00\x04")

        while True:
            while True:
                head = conn.recv(4)

                if head == b"":
                    break

                size_size = self.head2size_size[head]

                size_data = conn.recv(size_size)
                size = int.from_bytes(size_data, "big", signed=False)

                data = conn.recv(size)

                client.receive_queue.append((head, size, data))

            for package in client.send_queue:
                conn.send(package)
            client.send_queue.clear()

    def disconnect(self):
        pass


class RemoteNetworkConnector:
    """
    The thing on the client connecting to the server
    """

    def __init__(self):
        self.socket: typing.Optional[socket.socket] = None

        self.send_queue = []
        self.receive_queue = []

        self.head2size_size = {}

    def client_main(self):
        host = socket.gethostname()
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server

        self.socket = client_socket

    def send(self, data: bytes):
        self.send_queue.append(data)

    def handle(self):
        while True:
            head = self.socket.recv(4)

            if head == b"":
                break

            size_size = self.head2size_size[head]

            size_data = self.socket.recv(size_size)
            size = int.from_bytes(size_data, "big", signed=False)

            data = self.socket.recv(size)

            self.receive_queue.append((head, size, data))

        for data in self.send_queue:
            self.socket.send(data)

    def disconnect(self):
        self.socket.close()
