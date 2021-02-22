import mcpython.common.block.BlockState


class Block:
    def __init__(self, destroyed_by_explosion=True, destroyed_by_player=True):
        self.destroyed_by_explosion = destroyed_by_explosion
        self.destroyed_by_player = destroyed_by_player

    def on_creation(self, state: mcpython.common.block.BlockState.BlockState):
        pass

    def on_destroy(self, state: mcpython.common.block.BlockState.BlockState):
        pass

    def can_be_destroyed_by_explosion(
        self,
        state: mcpython.common.block.BlockState.BlockState,
        explosion_strength: float,
        explosion_distance: float,
    ) -> bool:
        return self.destroyed_by_explosion

    def can_be_destroyed_by_player(
        self, state: mcpython.common.block.BlockState.BlockState, player
    ) -> bool:
        return self.destroyed_by_player
