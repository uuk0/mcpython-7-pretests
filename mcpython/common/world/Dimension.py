import typing


class Dimension:
    def __init__(self):
        # The world this dimension is in
        self.world = None

        # The name of the dimension
        self.name: typing.Optional[str] = None

        # The internal id, assigned when None during saving the world, corrected when loading a world
        self.internal_id: typing.Optional[int] = None

        # A dict chunk pos -> Chunk, holding all loaded chunks
        self.chunks = {}

        # The player list for this dimension
        self.players = {}

        # The world generation driver for this dimension todo: implement
        self.world_generation_driver = None

    def get_chunk(
        self, position: typing.Tuple[int, int], load_from_files=True, generate=False
    ):
        raise NotImplementedError

    def get_chunk_for_position(
        self,
        position: typing.Union[typing.Tuple[int, int], typing.Tuple[int, int, int]],
        load_from_files=True,
        generate=False,
    ):
        return self.get_chunk(
            (position[0] // 16, position[-1] // 16),
            load_from_files=load_from_files,
            generate=generate,
        )

    def get_player(self, name: str, spawn_if_not_in_world=False):
        raise NotImplementedError

    def save(self):
        """
        Saves this dimension to the save files, with everything in memory
        """

    def save_fast(self):
        """
        Faster, but unsafer variant of save()
        Saves only stuff marked as dirty
        """

    def load_from_files(self):
        """
        Loads general stuff from the save files
        Chunks are loaded separately when needed, beside force loaded ones
        """
