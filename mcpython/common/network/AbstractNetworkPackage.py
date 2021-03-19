import abc
import typing

import mcpython.common.event.Registry
import mcpython.common.network.NetworkSide


class AbstractPackage(mcpython.common.event.Registry.IRegistryContent, abc.ABC):
    """
    Representation of a package for serialization over the network

    NAME is a unique name. Each name gets an ID assigned during client/server handshake events
    If a package arrives at one side, it is deserialized automatically and put into the queue for the respective process

    A package should behave identical when "put" as it is on the other side of the network, without serialization
    This can happen on local worlds not open to lan.
    """

    # The process the target should be invoked on. Leave None for immediate execution
    TARGET_PROCESS: typing.Optional[str] = None

    # If the sender expects an answer, if True, package_id will be set to a value, and the answer(Package) works
    # on the receiving side to send a package back to the original sender
    SENDER_EXPECTS_ANSWER = False

    @classmethod
    def handle(cls, side: mcpython.common.network.NetworkSide.NetworkSide, package: "AbstractPackage"):
        """
        Called on the defined process above with the side we are on [Real side or None, not BOTH]
        :param side: the side
        :param package: the package
        """

    @classmethod
    def handle_answer(cls, side: mcpython.common.network.NetworkSide.NetworkSide, previous: "AbstractPackage", answer: "AbstractPackage"):
        """
        Called when SENDER_EXPECTS_ANSWER is True and an answer to this package is received additional to the handle()
        method of the answer package
        :param side: the side on
        :param previous: the package the answer is on
        :param answer: the answer package

        If the package defines a answer(), you are allowed to call it.
        Please remember, this package will not be informed by default in that case as their is a package in between
        """

    @classmethod
    def deserialize(cls, side: mcpython.common.network.NetworkSide.NetworkSide, data_stream):
        pass

    def __init__(self):
        # The id of the package, may be used for identification during callback, only set and serialized
        # when SENDER_EXPECTS_ANSWER is True
        self.package_id = -1

        # The package id of the previous package, only serialized when SENDER_EXPECTS_ANSWER is True
        self.previous_package = -1

    def serialize(self, side: mcpython.common.network.NetworkSide.NetworkSide, put_strean):
        pass

    def answer(self, package: "AbstractPackage"):
        assert self.SENDER_EXPECTS_ANSWER

        package.previous_package = self.package_id

        # todo: send to the other side

