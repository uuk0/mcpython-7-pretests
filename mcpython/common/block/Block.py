import mcpython.common.block.BlockState
import mcpython.data.codec.AbstractCodec
import mcpython.data.codec.BlockClassCodec


class Block(mcpython.data.codec.AbstractCodec.AbstractEncodeAble):
    """
    Block Class
    Every instance represents a block "type"
    """
    CODEC = mcpython.data.codec.BlockClassCodec.BLOCK_CODEC

    def __init__(
        self,
        name: str,
        destroyed_by_explosion=True,
        destroyed_by_player=True,
        default_model_state=None,
    ):
        self.name = name
        self.destroyed_by_explosion = destroyed_by_explosion
        self.destroyed_by_player = destroyed_by_player
        self.default_model_state = (
            default_model_state if default_model_state is not None else {}
        )

    def on_creation(self, state: mcpython.common.block.BlockState.BlockState):
        state.set_state(self.default_model_state)

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

    def on_state_change(
        self,
        state: mcpython.common.block.BlockState.BlockState,
        state_previous: dict,
        state_new: dict,
    ):
        pass
