class BlockState:
    def __init__(self):
        self.position = None
        self.dimension = None
        self.block_class = None
        self.block_state = {}  # todo: something else? frozen dict?
        self.nbt = {}

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
            and self.block_state == other.block_state
            and self.nbt == other.nbt
        )

    def set_state(self, state: dict):
        previous = self.block_state
        self.block_state = state
        self.block_class.on_state_change(self, previous, state)
        self.mark_dirty()
