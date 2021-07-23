import collections
import typing
import mcpython.util.math
import pyglet


class ReferenceNotBakedException(Exception):
    pass


class ModelReference:
    def __init__(self, name_or_instance: typing.Union[str, "Model"]):
        self.name = (
            name_or_instance
            if isinstance(name_or_instance, str)
            else name_or_instance.name
        )
        self.instance: typing.Optional["Model"] = (
            None if isinstance(name_or_instance, str) else name_or_instance
        )

    def add_requirements_to_inner_list(self, model_entry_set: typing.Set[str]):
        model_entry_set.add(self.name)

    def get(self) -> typing.Optional["Model"]:
        # todo: load if needed
        return self.instance


class ModelElement:
    def __init__(
        self,
        from_pos: typing.Tuple[float, float, float],
        to_pos: typing.Tuple[float, float, float],
        rotation=(0., 0., 0.),
        uv=(0, 0, 1, 1),
    ):
        pass

    def add_requirements_to_inner_list(
        self, model_entry_set: typing.Set[str], texture_reference_set: typing.Set[str]
    ):
        pass

    def bake(self):
        pass


class Model:
    def __init__(self):
        self.baked = False

        self.name: typing.Optional[str] = None
        self.parent: typing.Optional[ModelReference] = None
        self.parent_instance: typing.Optional["Model"] = None
        self.elements: typing.List[ModelElement] = []
        self.texture_names = collections.ChainMap()

    def add_requirements_to_inner_list(
        self, model_entry_set: typing.Set[str], texture_reference_set: typing.Set[str]
    ):
        if self.parent is not None:
            self.parent.add_requirements_to_inner_list(model_entry_set)

        for element in self.elements:
            element.add_requirements_to_inner_list(
                model_entry_set, texture_reference_set
            )

    def bake(self):
        if self.parent is not None:
            self.parent_instance = self.parent.get()
            if not self.parent_instance.baked:
                raise ReferenceNotBakedException

            self.texture_names.maps.extend(self.parent_instance.texture_names.maps)

            if len(self.elements) == 0:
                self.elements = (
                    self.parent_instance.elements
                )  # todo: something better here...

        self.baked = True

        for element in self.elements:
            element.bake()
