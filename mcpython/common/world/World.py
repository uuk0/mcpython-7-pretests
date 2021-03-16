import typing
import mcpython.common.world.Dimension


class World:
    """
    The world
    Holds information about the whole world
    """

    def __init__(self):
        # A dict name -> Dimension, holding all arrival dimensions
        self.dimensions: typing.Dict[
            str, mcpython.common.world.Dimension.Dimension
        ] = {}

        # A dict of name -> Player, holding all players in the world
        self.players = {}

        # How long the world is loaded in total, for statistics
        self.active_time = 0.0

        # Which players where in the world, used for checking for new spawn / load from save files spawn, and intro info's
        self.known_players: typing.Set[str] = set()

        # The controller wrapper for storage stuff, wraps stuff on the file i/o process todo: implement
        self.storage_controller = None

    def add_dimension(self, name: str, internal_id=None):
        dimension = self.dimensions.setdefault(
            name, mcpython.common.world.Dimension.Dimension()
        )
        dimension.name = name
        dimension.world = self
        return dimension

    def get_dimension(self, name: str):
        return self.dimensions[name]

    def remove_dimension(self, name: str):
        del self.dimensions[name]

    def make_dimension_loaded(self, name: str):
        if name not in self.dimensions:
            dimension = self.add_dimension(name)
        else:
            dimension = self.dimensions[name]

        dimension.load_from_files()

    def check_dimensions_for_unload(self):
        raise NotImplementedError

    def get_player(self, name: str, spawn_if_not_in_world=False):
        return self.players[name]
