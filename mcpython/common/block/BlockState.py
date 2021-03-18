class BlockState:
    """
    Class representing a block in the world.
    BlockState for historical reasons, it itself holds a state of the block (their the name from),
    but holds a lot more stuff internally

    todo: wrap the Block functions here without the state which is auto-passed
    """

    def __init__(self):
        self.position = None
        self.dimension = None
        self.block_class = None
        self.state = {}  # todo: something better
        self.nbt = {}  # todo: something better, maybe dynamically created?

        # Marks the block state "dirty", meaning it must be saved
        self.dirty = False

    def can_be_destroyed_by_explosion(
        self,
        explosion_strength: float,
        explosion_distance: float,
    ) -> bool:
        return self.block_class.can_be_destroyed_by_explosion(
            self, explosion_strength, explosion_distance
        )

    def can_be_destroyed_by_player(self, player) -> bool:
        return self.block_class.can_be_destroyed_by_player(self, player)

    # BlockState only

    def mark_dirty(self):
        self.dirty = True

    def equal_type(self, other: "BlockState"):
        return (
            self.block_class == other.block_class
            and self.state == other.state
            and self.nbt == other.nbt
        )

    def set_state(self, state: dict):
        previous = self.state
        self.state = state
        self.block_class.on_state_change(self, previous, state)
        self.mark_dirty()
