class BlockState:
    def __init__(self):
        self.position = None
        self.dimension = None
        self.block_class = None

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
