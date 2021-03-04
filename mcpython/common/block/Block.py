from mcpython.common.block import BlockState
import mcpython.data.codec.AbstractCodec


class Block(mcpython.data.codec.AbstractCodec.AbstractEncodeAble):
    """
    Block Class
    Every instance represents a block "type"
    """

    @classmethod
    def get_codec(cls):
        import mcpython.data.codec.BlockClassCodec

        return mcpython.data.codec.BlockClassCodec.BLOCK_CODEC

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

    def on_creation(self, state: BlockState):
        state.set_state(self.default_model_state)

    def on_destroy(self, state: BlockState):
        pass

    def can_be_destroyed_by_explosion(
        self,
        state: BlockState,
        explosion_strength: float,
        explosion_distance: float,
    ) -> bool:
        return self.destroyed_by_explosion

    def can_be_destroyed_by_player(self, state: BlockState, player) -> bool:
        return self.destroyed_by_player

    def on_state_change(
        self,
        state: BlockState,
        state_previous: dict,
        state_new: dict,
    ):
        pass

    def __repr__(self):
        return "MinecraftBlockType(name={})".format(self.name)
