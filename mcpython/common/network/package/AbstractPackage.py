from abc import ABC
from mcpython import shared


class AbstractPackage(ABC):
    BUS: str = None
    NAME: str = None
    PACKAGE_SIZE_SIZE: int = 2

    INTERNAL_PACKAGE_ID: bytes = None

    @classmethod
    def deserialize(cls, data: bytes) -> "AbstractPackage":
        raise NotImplementedError

    def __init__(self):
        self.package_id = None
        self.answer_of = None

    def serialize(self) -> bytes:
        raise NotImplementedError

    def send_to(self, target: int):
        pass


class DefaultPackage(AbstractPackage, ABC):
    def serialize(self) -> bytes:
        body = self.serialize_internal()
        return self.INTERNAL_PACKAGE_ID + len(body).to_bytes(self.PACKAGE_SIZE_SIZE, "big", signed=False) + body

    def serialize_internal(self) -> bytes:
        raise NotImplementedError

