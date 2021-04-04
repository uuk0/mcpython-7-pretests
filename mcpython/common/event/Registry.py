import typing
from abc import ABC


class IRegistryContent(ABC):
    """
    Base class for content for registries
    Contains the NAME attribute for identification, and the event functions called on
    register/unregister
    """

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
    A registry is a container of multiple sub-types of something more general
    It is a semi-dynamic structure, build for dynamic holding stuff, exchanging stuff during reload,
        but also storing stable stuff
    """

    def __init__(
        self,
        name: str,
        *accepted_base_classes: typing.Type[IRegistryContent],
        target_is_class=False,
        register_not_namespace_variants=True,
    ):
        """
        Creates a new registry
        :param name: the name of the registry, should be namespace-ed
        :param accepted_base_classes: which IRegistryContent classes to accept as base-classes
        :param target_is_class: if the target in the registry is a class, or otherwise a object, so a instance of a class
        :param register_not_namespace_variants: if special_content should contain variants without the namespace
        """
        self.name = name
        self.accepted_base_classes: typing.Iterable[
            typing.Type[IRegistryContent]
        ] = accepted_base_classes
        self.target_is_class: bool = target_is_class
        self.register_not_namespace_variants: bool = register_not_namespace_variants

        # The content of the registry, as a map NAME -> object
        self.content: typing.Dict[
            str, typing.Union[IRegistryContent, typing.Type[IRegistryContent]]
        ] = {}
        # The special content of the registry, as UN-NAMESPACE-ED NAME -> object[]
        self.special_content: typing.Dict[
            str,
            typing.List[typing.Union[IRegistryContent, typing.Type[IRegistryContent]]],
        ] = {}

    def register(
        self,
        obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]],
        validate=True,
        override_existing=True,
        call_obj_register_event=True,
    ):
        """
        Registers a object into the registry
        :param obj: the object
        :param validate: if validation of the object should occur
        :param override_existing: if existing objects in registry should be replaced by this (they are removed
            from the registry)
        :param call_obj_register_event: if the object should be informed that it is now part of this registry
        :return: the object itself
        """
        assert not validate or self.validate(obj), (
            "object is invalid in registry " + self.name
        )
        assert obj.NAME is not None, f"NAME must be set on object {obj}"

        if obj.NAME in self.content:
            if override_existing:
                self.unregister(
                    self.content[obj.NAME],
                    validate=False,
                    remove_special_if_empty=False,
                )
            else:
                raise ValueError(
                    f"an object named {obj.NAME} exists in registry {self.name} (tried to register {obj})"
                )

        self.content[obj.NAME] = obj

        if self.register_not_namespace_variants and obj.NAME.count(":") == 1:
            self.special_content.setdefault(obj.NAME.split(":")[-1], []).append(obj)

        if call_obj_register_event:
            obj.on_register(self)

        return obj

    def unregister(
        self,
        obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]],
        validate=True,
        skip_on_missing=False,
        remove_special_if_empty=True,
        call_obj_unregister_event=True,
    ):
        """
        Removes an object from the registry
        :param obj: the object
        :param validate: if validation should occur on the object
        :param skip_on_missing: skip if object not in registry
        :param remove_special_if_empty: remove the entry in special_content if it is empty after removal
        :param call_obj_unregister_event: if the unregister event should be called on the object or not
        :return: the object
        """
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

        if call_obj_unregister_event:
            obj.on_unregister(self)

        return obj

    def validate(
        self, obj: typing.Union[IRegistryContent, typing.Type[IRegistryContent]]
    ) -> bool:
        """
        Returns if the object is valid in this registry
        :param obj: the object to check
        """
        if self.target_is_class:
            return issubclass(obj, tuple(self.accepted_base_classes))

        return isinstance(obj, tuple(self.accepted_base_classes))
