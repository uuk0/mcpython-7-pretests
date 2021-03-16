from mcpython.common.block import BlockState
import mcpython.data.codec.AbstractCodec


class Block(mcpython.data.codec.AbstractCodec.AbstractEncodeAble):
    """
    Block Class
    Every instance represents a block "type"
    See BlockState for the representation in the world
    You may create instances of this or subclass and create than instances.
    You may exchange the BlockState class for advanced functionality. See the stuff there
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

        self.material = None
        self.map_color = None
        self.requires_tool = False
        self.hardness = 0
        self.blast_resistance = 0
        self.ticks_randomly = False
        self.sound_group = None
        self.has_collision = True
        self.breaks_instantly = False
        self.drops_nothing = False
        self.opaque = True
        self.solid = True
        self.allow_spawns = True
        self.do_suffocation = True
        self.blocks_vision = True
        self.dynamic_bounds = False
        self.drops_like = None

    def setMaterial(self, material: str):
        self.material = material
        return self

    def setMapColor(self, color: str):
        self.map_color = color
        return self

    def requiresTool(self):
        self.requires_tool = True
        return self

    def strength(self, hardness: float, blast_resistance=None):
        self.hardness = hardness
        self.blast_resistance = (
            blast_resistance if blast_resistance is not None else hardness
        )
        return self

    def ticksRandomly(self):
        self.ticks_randomly = True
        return self

    def sounds(self, group: str):
        self.sound_group = group
        return self

    def noCollision(self):
        self.has_collision = False
        return self

    def breakInstantly(self):
        self.breaks_instantly = True
        return self

    def dropsNothing(self):
        self.drops_nothing = True
        return self

    def nonOpaque(self):
        self.opaque = False
        return self

    def nonSolid(self):
        self.solid = False
        return self

    def noSpawning(self):
        self.allow_spawns = False
        return self

    def noSuffocation(self):
        self.do_suffocation = False
        return self

    def noVisionBlock(self):
        self.blocks_vision = False
        return self

    def dynamicBounds(self):
        self.dynamic_bounds = True
        return self

    def dropsLike(self, block: str):
        self.drops_like = block
        return self

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

    def can_be_destroyed_by_player(
        self, state: BlockState, player, hand, held_itemstack
    ) -> bool:
        return self.destroyed_by_player

    def on_state_change(
        self,
        state: BlockState,
        state_previous: dict,
        state_new: dict,
    ) -> bool:
        return True

    def is_solid(
        self,
        state: BlockState,
        side=None,
    ):
        return self.solid

    def can_spawn_entity_on(
        self,
        state: BlockState,
        entity,
    ) -> bool:
        return self.allow_spawns

    def get_current_model_state(self, state: BlockState):
        return self.default_model_state

    def __repr__(self):
        return "MinecraftBlockType(name='{}')".format(self.name)
