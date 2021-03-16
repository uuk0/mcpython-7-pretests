import typing


class World:
    """
    The world
    Holds information about the whole world
    """

    def __init__(self):
        # A dict name -> Dimension, holding all arrival dimensions
        self.dimensions = {}

        # A dict of name -> Player, holding all players in the world
        self.players = {}

        # How long the world is loaded in total, for statistics
        self.active_time = 0.0

        # Which players where in the world, used for checking for new spawn / load from save files spawn, and intro info's
        self.known_players: typing.Set[str] = set()

        # The controller wrapper for storage stuff, wraps stuff on the file i/o process todo: implement
        self.storage_controller = None

    def add_dimension(self, name: str, internal_id=None):
        raise NotImplementedError

    def get_dimension(self, name: str):
        raise NotImplementedError

    def remove_dimension(self, name: str):
        raise NotImplementedError

    def make_dimension_loaded(self, name: str):
        raise NotImplementedError

    def check_dimensions_for_unload(self):
        raise NotImplementedError

    def get_player(self, name: str, spawn_if_not_in_world=False):
        raise NotImplementedError
