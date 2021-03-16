import typing
from abc import ABC


class IRegistryContent(ABC):
    NAME = None

    @classmethod
    def on_register(cls, registry: "Registry"):
        pass

    @classmethod
    def on_unregister(cls, registry: "Registry"):
        pass


class Registry:
    """
    Class for every registry
    """

    def __init__(
        self,
        name: str,
        *accepted_base_classes,
        target_is_class=False,
        register_not_namespace_variants=True,
    ):
        self.register_not_namespace_variants = register_not_namespace_variants
        self.name = name
        self.accepted_base_classes = accepted_base_classes
        self.target_is_class = target_is_class

        self.content = {}
        self.special_content = {}

    def register(
        self,
        obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]],
        validate=True,
    ):
        assert not validate or self.validate(obj), (
            "object is invalid in registry " + self.name
        )

        self.content[obj.NAME] = obj

        if self.register_not_namespace_variants and obj.NAME.count(":") == 1:
            self.special_content.setdefault(obj.NAME.split(":")[-1], []).append(obj)

        obj.on_register(self)

        return obj

    def unregister(
        self,
        obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]],
        validate=True,
        skip_on_missing=False,
        remove_special_if_empty=True,
    ):
        assert not validate or self.validate(obj), (
            "object is invalid in registry " + self.name
        )

        if obj.NAME not in self.content or self.content[obj.NAME] != obj:
            if skip_on_missing:
                return
            raise ValueError(
                f"content {obj} in registry {self.name} not found scheduled for unregister"
            )

        del self.content[obj.NAME]

        if self.register_not_namespace_variants:
            name = obj.NAME.split(":")[-1]
            self.special_content[name].remove(obj)

            if remove_special_if_empty and len(self.special_content[name]) == 0:
                del self.special_content[name]

        obj.on_unregister(self)

        return obj

    def validate(self, obj):
        if self.target_is_class:
            return issubclass(obj, self.accepted_base_classes)

        return isinstance(obj, self.accepted_base_classes)
