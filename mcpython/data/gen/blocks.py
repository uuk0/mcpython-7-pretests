from mcpython.data.gen.Driver import driver
from mcpython.common.block.Block import Block

COLORS = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray",
          "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"]


# This is the only stuff needed, everything else happens behind the scenes
# missing: air
driver.add_target(Block("minecraft:stone").setMaterial("stone").setMapColor("stone_gray").requiresTool().strength(1.5, 6.0))
driver.add_target(Block("minecraft:granite").setMaterial("stone").setMaterial("dirt_brown").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:polished_granite").setMaterial("stone").setMaterial("dirt_brown").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:diorite").setMaterial("stone").setMaterial("off_white").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:polished_diorite").setMaterial("stone").setMaterial("off_white").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:andesite").setMaterial("stone").setMaterial("stone_gray").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:polished_andesite").setMaterial("stone").setMaterial("stone_gray").requiresTool().strength(1.6, 6.0))
driver.add_target(Block("minecraft:grass_block").setMaterial("solid_organic").ticksRandomly().strength(.6).sounds("grass"), plugins=[("minecraft:grass_block_transfer", "minecraft:grass_block", "minecraft:dirt")])
driver.add_target(Block("minecraft:dirt").setMaterial("soil").setMapColor("dirt_brown").strength(.5).sounds("gravel"))
driver.add_target(Block("minecraft:coarse_dirt").setMaterial("soil").setMapColor("dirt_brown").strength(.5).sounds("gravel"))
driver.add_target(Block("minecraft:podzol").setMaterial("soil").setMapColor("spruce_brown").strength(.5).sounds("gravel"), plugins=[("minecraft:snowy_block",)])
driver.add_target(Block("minecraft:cobblestone").setMaterial("stone").requiresTool().strength(2.0, 6.0))
driver.add_target(Block("minecraft:bricks").setMaterial("stone").setMapColor("red").requiresTool().strength(2.0, 6.0))
driver.add_target(Block("minecraft:mossy_cobblestone").setMaterial("stone").requiresTool().strength(2.0, 6.0))
driver.add_target(Block("minecraft:obsidian").setMaterial("stone").requiresTool().strength(50.0, 1200.0))
driver.add_target(Block("minecraft:farmland").setMaterial("soil").ticksRandomly().strength(0.6).sounds("gravel"), plugins=[("minecraft:farmland_like",)])

driver.add_target(Block("minecraft:oak_planks").setMaterial("wood").setMapColor("oak_tan").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:spruce_planks").setMaterial("wood").setMapColor("spruce_brown").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:birch_planks").setMaterial("wood").setMapColor("pale_yellow").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:jungle_planks").setMaterial("wood").setMapColor("dirt_brown").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:acacia_planks").setMaterial("wood").setMapColor("orange").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:dark_oak_planks").setMaterial("wood").setMapColor("brown").strength(2.0, 3.0).sounds("wood"))
driver.add_target(Block("minecraft:oak_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:oak_tree_pool")])
driver.add_target(Block("minecraft:spruce_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:spruce_tree_pool")])
driver.add_target(Block("minecraft:birch_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:birch_tree_pool")])
driver.add_target(Block("minecraft:jungle_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:jungle_tree_pool")])
driver.add_target(Block("minecraft:acacia_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:acacia_tree_pool")])
driver.add_target(Block("minecraft:dark_oak_saplings").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:sapling", "minecraft:dark_oak_tree_pool")])

driver.add_target(Block("minecraft:bedrock").setMaterial("stone").strength(-1, 3600000).dropsNothing(), plugins=[("minecraft:spawns", [], [])])
driver.add_target(Block("minecraft:water").setMaterial("water").noCollision().strength(100).dropsNothing(), plugins=[("minecraft:water_like_liquid",)])
driver.add_target(Block("minecraft:lava").setMaterial("lava").noCollision().ticksRandomly().strength(100).dropsNothing(), plugins=[("minecraft:lava_like_liquid",), ("minecraft:luminance", 15)])
driver.add_target(Block("minecraft:sand").setMaterial("aggregate").setMapColor("pale_yellow").strength(0.5).sounds("sand"), plugins=[("minecraft:falling_block",), ("minecraft:sand", 14406560)])
driver.add_target(Block("minecraft:red_sand").setMaterial("aggregate").setMapColor("orange").strength(0.5).sounds("sand"), plugins=[("minecraft:falling_block",), ("minecraft:sand", 11098145)])
driver.add_target(Block("minecraft:gravel").setMaterial("aggregate").setMapColor("stone_gray").strength(0.6).sounds("gravel"), plugins=[("minecraft:falling_block",)])

driver.add_target(Block("minecraft:gold_ore").setMaterial("stone").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:deepslate_gold_ore").setMaterial("stone").requiresTool().strength(4.0, 3.0).sounds("deepslate"))
driver.add_target(Block("minecraft:nether_gold_ore").setMaterial("stone").setMapColor("dark_red").requiresTool().strength(3.0).sounds("nether_gold_ore"))
driver.add_target(Block("minecraft:iron_ore").setMaterial("stone").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:deepslate_iron_ore").setMaterial("stone").requiresTool().strength(4.5, 3.0).sounds("deepslate"))
driver.add_target(Block("minecraft:coal_ore").setMaterial("stone").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:lapis_ore").setMaterial("stone").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:deepslate_lapis_ore").setMaterial("stone").requiresTool().strength(4.5, 3.0).sounds("deepslate"))
driver.add_target(Block("minecraft:diamond_ore").setMaterial("stone").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:deepslate_diamond_ore").setMaterial("stone").requiresTool().strength(4.5, 3.0).sounds("deepslate"))

driver.add_target(Block("minecraft:lapis_block").setMaterial("metal").setMapColor("lapis_blue").requiresTool().strength(3.0))
driver.add_target(Block("minecraft:gold_block").setMaterial("metal").setMapColor("gold").requiresTool().strength(3.0, 6.0).sounds("metal"))
driver.add_target(Block("minecraft:iron_block").setMaterial("metal").setMapColor("iron_gray").requiresTool().strength(5.0, 6.0).sounds("metal"))
driver.add_target(Block("minecraft:diamond_block").setMaterial("metal").setMapColor("diamond_blue").requiresTool().strength(5.0, 6.0).sounds("metal"))

driver.add_target(Block("minecraft:oak_log"), plugins=[("minecraft:log", "oak_tan", "spruce_brown")])
driver.add_target(Block("minecraft:spruce_log"), plugins=[("minecraft:log", "spruce_brown", "brown")])
driver.add_target(Block("minecraft:birch_log"), plugins=[("minecraft:log", "pale_yellow", "off_white")])
driver.add_target(Block("minecraft:jungle_log"), plugins=[("minecraft:log", "dirt_brown", "spruce_brown")])
driver.add_target(Block("minecraft:acacia_log"), plugins=[("minecraft:log", "orange", "stone_gray")])
driver.add_target(Block("minecraft:dark_oak_log"), plugins=[("minecraft:log", "brown", "brown")])
driver.add_target(Block("minecraft:stripped_oak_log"), plugins=[("minecraft:log", "oak_tan", "oak_tan")])
driver.add_target(Block("minecraft:stripped_spruce_log"), plugins=[("minecraft:log", "spruce_brown", "spruce_brown")])
driver.add_target(Block("minecraft:stripped_birch_log"), plugins=[("minecraft:log", "pale_yellow", "pale_yellow")])
driver.add_target(Block("minecraft:stripped_jungle_log"), plugins=[("minecraft:log", "dirt_brown", "dirt_brown")])
driver.add_target(Block("minecraft:stripped_acacia_log"), plugins=[("minecraft:log", "orange", "orange")])
driver.add_target(Block("minecraft:stripped_dark_oak_log"), plugins=[("minecraft:log", "brown", "brown")])

driver.add_target(Block("minecraft:oak_wood").strength(2.0).sounds("wood").setMapColor("oak_tan").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:spruce_wood").strength(2.0).sounds("wood").setMapColor("spruce_brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:birch_wood").strength(2.0).sounds("wood").setMapColor("pale_yellow").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:jungle_wood").strength(2.0).sounds("wood").setMapColor("dirt_brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:acacia_wood").strength(2.0).sounds("wood").setMapColor("gray").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:dark_oak_wood").strength(2.0).sounds("wood").setMapColor("brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_oak_wood").strength(2.0).sounds("wood").setMapColor("oak_tan").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_spruce_wood").strength(2.0).sounds("wood").setMapColor("spruce_brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_birch_wood").strength(2.0).sounds("wood").setMapColor("pale_yellow").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_jungle_wood").strength(2.0).sounds("wood").setMapColor("dirt_brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_acacia_wood").strength(2.0).sounds("wood").setMapColor("orange").setMaterial("wood"), plugins=[("minecraft:pillar",)])
driver.add_target(Block("minecraft:stripped_dark_oak_wood").strength(2.0).sounds("wood").setMapColor("brown").setMaterial("wood"), plugins=[("minecraft:pillar",)])

driver.add_target(Block("minecraft:oak_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])
driver.add_target(Block("minecraft:spruce_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])
driver.add_target(Block("minecraft:birch_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])
driver.add_target(Block("minecraft:jungle_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])
driver.add_target(Block("minecraft:acacia_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])
driver.add_target(Block("minecraft:dark_oak_leaves").sounds("grass"), plugins=[("minecraft:leaves",)])

driver.add_target(Block("minecraft:azalea_leaves").sounds("azalea_leaves"), plugins=[("minecraft:leaves_azalea",)])
driver.add_target(Block("minecraft:azalea_leaves_flowers").sounds("azalea_leaves"), plugins=[("minecraft:leaves_azalea",)])

driver.add_target(Block("minecraft:sponge").setMaterial("sponge").strength(0.6).sounds("grass"), plugins=[("minecraft:sponge", "#minecraft:removed_by_sponge_to_wet", "#minecraft:removed_by_sponge_gone")])
driver.add_target(Block("minecraft:wet_sponge").setMaterial("sponge").strength(0.6).sounds("grass"), plugins=[("minecraft:wet_sponge", "#minecraft:dries_sponge")])

driver.add_target(Block("minecraft:glass").setMaterial("glass").strength(0.3).sounds("glass").nonOpaque().nonSolid().noSpawning().noSuffocation().noVisionBlock())

driver.add_target(Block("minecraft:dispenser").setMaterial("stone").requiresTool().strength(3.5), plugins=[("minecraft:dispenser_like",)])

driver.add_target(Block("minecraft:sandstone").setMaterial("stone").setMapColor("pale_yellow").requiresTool().strength(0.8))
driver.add_target(Block("minecraft:chiseled_sandstone").setMaterial("stone").setMapColor("pale_yellow").requiresTool().strength(0.8))
driver.add_target(Block("minecraft:cut_sandstone").setMaterial("stone").setMapColor("pale_yellow").requiresTool().strength(0.8))

# todo: add some registry for blocks for sounds linked in the properties of the plugin
driver.add_target(Block("minecraft:note_block").setMaterial("wood").sounds("wood").strength(0.8), plugins=[("minecraft:note_block_like",)])

for c in COLORS:
    driver.add_target(Block(f"minecraft:{c}_bed"), plugins=[("minecraft:bed", c)])
    driver.add_target(Block(f"minecraft:{c}_wool").setMaterial("wool").setMapColor(c).strength(0.8).sounds("wool"))

driver.add_target(Block("minecraft:powered_rail").setMaterial("decoration").noCollision().strength(0.7).sounds("metal"), plugins=[("minecraft:powered_rail", 1)])
driver.add_target(Block("minecraft:detector_rail").setMaterial("decoration").noCollision().strength(0.7).sounds("metal"), plugins=[("minecraft:detector_rail", 1, 15)])

driver.add_target(Block("minecraft:sticky_piston"), plugins=[("minecraft:sticky_piston", 12, 12)])
driver.add_target(Block("minecraft:piston"), plugins=[("minecraft:normal_piston", 12)])
driver.add_target(Block("minecraft:piston_head").setMaterial("piston").strength(1.5).dropsNothing(), plugins=[("minecraft:piston_head",)])
driver.add_target(Block("minecraft:moving_piston").setMaterial("piston").strength(-1).dynamicBounds().dropsNothing().nonOpaque().nonSolid().noSuffocation().noVisionBlock(), plugins=[("minecraft:moving_piston",)])

driver.add_target(Block("minecraft:cobweb").setMaterial("cobweb").noCollision().requiresTool().strength(4.0), plugins=[("minecraft:cobweb",)])

driver.add_target(Block("minecraft:grass").setMaterial("replaceable_plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:fern_like",)])
driver.add_target(Block("minecraft:fern").setMaterial("replaceable_plant").setMapColor("oak_tan").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:fern_like",)])
driver.add_target(Block("minecraft:dead_bush").setMaterial("replaceable_plant").setMapColor("oak_tan").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:fern_like",)])
driver.add_target(Block("minecraft:seagrass").setMaterial("replaceable_underwater_plant").noCollision().breakInstantly().sounds("wet_grass"), plugins=[("minecraft:seagrass_like",)])
driver.add_target(Block("minecraft:tall_seagrass").setMaterial("replaceable_underwater_plant").noCollision().breakInstantly().sounds("wet_grass"), plugins=[("minecraft:tall_seagrass_like",)])

driver.add_target(Block("minecraft:dandelion").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:saturation")])
driver.add_target(Block("minecraft:poppy").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:night_vision")])
driver.add_target(Block("minecraft:blue_orchid").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:saturation")])
driver.add_target(Block("minecraft:allium").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:fire_resistance")])
driver.add_target(Block("minecraft:azure_bluet").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:blindness")])
driver.add_target(Block("minecraft:red_tulip").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:weakness")])
driver.add_target(Block("minecraft:orange_tulip").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:weakness")])
driver.add_target(Block("minecraft:white_tulip").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:weakness")])
driver.add_target(Block("minecraft:pink_tulip").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:weakness")])
driver.add_target(Block("minecraft:oxeye_daisy").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:regeneration")])
driver.add_target(Block("minecraft:cornflower").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:jump_boost")])
driver.add_target(Block("minecraft:wither_rose").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:wither")])
driver.add_target(Block("minecraft:lily_of_the_valley").setMaterial("plant").noCollision().breakInstantly().sounds("grass"), plugins=[("minecraft:flower",), ("minecraft:suspicious_stew", "minecraft:poison")])
driver.add_target(Block("minecraft:brown_mushroom").setMaterial("plant").setMapColor("brown").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:mushroom",), ("minecraft:luminance", 1), ("minecraft:sapling2tree_bonemeal", "minecraft:huge_brown_mushroom")])
driver.add_target(Block("minecraft:red_mushroom").setMaterial("plant").setMapColor("red").noCollision().ticksRandomly().breakInstantly().sounds("grass"), plugins=[("minecraft:mushroom",), ("minecraft:luminance", 1), ("minecraft:sapling2tree_bonemeal", "minecraft:huge_red_mushroom")])

# todo: the explosive number may not be correct
driver.add_target(Block("minecraft:tnt").setMaterial("tnt").breakInstantly().sounds("grass"), plugins=[("minecraft:explosive", 10)])

driver.add_target(Block("minecraft:bookshelf").setMaterial("wood").strength(1.5).sounds("wood"))

driver.add_target(Block("minecraft:torch").setMaterial("decoration").noCollision().breakInstantly().sounds("wood"), plugins=[("minecraft:torch", "minecraft:flame"), ("minecraft:luminance", 14)])
driver.add_target(Block("minecraft:wall_torch").setMaterial("decoration").noCollision().breakInstantly().sounds("wood").dropsLike("minecraft:torch"), plugins=[("minecraft:wall_torch", "minecraft:flame"), ("minecraft:luminance", 14)])
driver.add_target(Block("minecraft:fire").setMaterial("fire").setMapColor("bright_red").noCollision().breakInstantly().sounds("wool"), plugins=[("minecraft:luminance", 15)])
driver.add_target(Block("minecraft:soul_fire").setMaterial("fire").setMapColor("light_blue").noCollision().breakInstantly().sounds("wool"), plugins=[("minecraft:luminance", 15)])

driver.add_target(Block("minecraft:spawner").setMaterial("stone").requiresTool().strength(0.5).sounds("metal").nonOpaque(), plugins=[("minecraft:spawner/all",)])

driver.add_target(Block("minecraft:oak_stairs").setMaterial("wood").setMapColor("oak_tan").strength(2.0, 3.0).sounds("wood"), plugins=[("minecraft:stair",)])

# todo: add container classes
driver.add_target(Block("minecraft:chest").setMaterial("wood").strength(2.5).sounds("wood"), plugins=[("minecraft:block_stationary_container", None,)])
driver.add_target(Block("minecraft:crafting_table").setMaterial("wood").strength(2.5).sounds("wood"), plugins=[("minecraft:player_stationary_container", None)])
driver.add_target(Block("minecraft:furnace").setMaterial("stone").requiresTool().strength(3.5), plugins=[("minecraft:luminance", 13), ("minecraft:block_stationary_container", None,)])

driver.add_target(Block("minecraft:redstone_wire").setMaterial("decoration").noCollision().breakInstantly())

driver.add_target(Block("minecraft:wheat").setMaterial("plant").noCollision().ticksRandomly().breakInstantly().sounds("crop"))
"""
OAK_SIGN = register("oak_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.OAK));
SPRUCE_SIGN = register("spruce_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD, SPRUCE_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.SPRUCE));
BIRCH_SIGN = register("birch_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.PALE_YELLOW).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.BIRCH));
ACACIA_SIGN = register("acacia_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.ORANGE).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.ACACIA));
JUNGLE_SIGN = register("jungle_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD, JUNGLE_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.JUNGLE));
DARK_OAK_SIGN = register("dark_oak_sign", new SignBlock(AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.DARK_OAK));
OAK_DOOR = register("oak_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, OAK_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
LADDER = register("ladder", new LadderBlock(AbstractBlock.Settings.of(Material.DECORATION).strength(0.4F).sounds(BlockSoundGroup.LADDER).nonOpaque()));
RAIL = register("rail", new RailBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.7F).sounds(BlockSoundGroup.METAL)));
COBBLESTONE_STAIRS = register("cobblestone_stairs", new StairsBlock(COBBLESTONE.getDefaultState(), AbstractBlock.Settings.copy(COBBLESTONE)));
OAK_WALL_SIGN = register("oak_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(OAK_SIGN), SignType.OAK));
SPRUCE_WALL_SIGN = register("spruce_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD, SPRUCE_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(SPRUCE_SIGN), SignType.SPRUCE));
BIRCH_WALL_SIGN = register("birch_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.PALE_YELLOW).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(BIRCH_SIGN), SignType.BIRCH));
ACACIA_WALL_SIGN = register("acacia_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.ORANGE).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(ACACIA_SIGN), SignType.ACACIA));
JUNGLE_WALL_SIGN = register("jungle_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD, JUNGLE_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(JUNGLE_SIGN), SignType.JUNGLE));
DARK_OAK_WALL_SIGN = register("dark_oak_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_LOG.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(DARK_OAK_SIGN), SignType.DARK_OAK));
LEVER = register("lever", new LeverBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
STONE_PRESSURE_PLATE = register("stone_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.MOBS, AbstractBlock.Settings.of(Material.STONE).requiresTool().noCollision().strength(0.5F)));
IRON_DOOR = register("iron_door", new DoorBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.IRON_GRAY).requiresTool().strength(5.0F).sounds(BlockSoundGroup.METAL).nonOpaque()));
OAK_PRESSURE_PLATE = register("oak_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, OAK_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
SPRUCE_PRESSURE_PLATE = register("spruce_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, SPRUCE_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
BIRCH_PRESSURE_PLATE = register("birch_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, BIRCH_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
JUNGLE_PRESSURE_PLATE = register("jungle_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, JUNGLE_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
ACACIA_PRESSURE_PLATE = register("acacia_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, ACACIA_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
DARK_OAK_PRESSURE_PLATE = register("dark_oak_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
REDSTONE_ORE = register("redstone_ore", new RedstoneOreBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().ticksRandomly().luminance(createLightLevelFromLitBlockState(9)).strength(3.0F, 3.0F)));
DEEPSLATE_REDSTONE_ORE = register("deepslate_redstone_ore", new RedstoneOreBlock(AbstractBlock.Settings.copy(REDSTONE_ORE).strength(4.5F, 3.0F).sounds(BlockSoundGroup.DEEPSLATE)));
REDSTONE_TORCH = register("redstone_torch", new RedstoneTorchBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().breakInstantly().luminance(createLightLevelFromLitBlockState(7)).sounds(BlockSoundGroup.WOOD)));
REDSTONE_WALL_TORCH = register("redstone_wall_torch", new WallRedstoneTorchBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().breakInstantly().luminance(createLightLevelFromLitBlockState(7)).sounds(BlockSoundGroup.WOOD).dropsLike(REDSTONE_TORCH)));
STONE_BUTTON = register("stone_button", new StoneButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F)));
SNOW = register("snow", new SnowBlock(AbstractBlock.Settings.of(Material.SNOW_LAYER).ticksRandomly().strength(0.1F).requiresTool().sounds(BlockSoundGroup.SNOW)));
ICE = register("ice", new IceBlock(AbstractBlock.Settings.of(Material.ICE).slipperiness(0.98F).ticksRandomly().strength(0.5F).sounds(BlockSoundGroup.GLASS).nonOpaque().allowsSpawning((state, world, pos, entityType) -> {
 return entityType == EntityType.POLAR_BEAR;
})));
SNOW_BLOCK = register("snow_block", new Block(AbstractBlock.Settings.of(Material.SNOW_BLOCK).requiresTool().strength(0.2F).sounds(BlockSoundGroup.SNOW)));
CACTUS = register("cactus", new CactusBlock(AbstractBlock.Settings.of(Material.CACTUS).ticksRandomly().strength(0.4F).sounds(BlockSoundGroup.WOOL)));
CLAY = register("clay", new Block(AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.6F).sounds(BlockSoundGroup.GRAVEL)));
SUGAR_CANE = register("sugar_cane", new SugarCaneBlock(AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.GRASS)));
JUKEBOX = register("jukebox", new JukeboxBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.DIRT_BROWN).strength(2.0F, 6.0F)));
OAK_FENCE = register("oak_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, OAK_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
PUMPKIN = register("pumpkin", new PumpkinBlock(AbstractBlock.Settings.of(Material.GOURD, MapColor.ORANGE).strength(1.0F).sounds(BlockSoundGroup.WOOD)));
NETHERRACK = register("netherrack", new NetherrackBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(0.4F).sounds(BlockSoundGroup.NETHERRACK)));
SOUL_SAND = register("soul_sand", new SoulSandBlock(AbstractBlock.Settings.of(Material.AGGREGATE, MapColor.BROWN).strength(0.5F).velocityMultiplier(0.4F).sounds(BlockSoundGroup.SOUL_SAND).allowsSpawning(Blocks::always).solidBlock(Blocks::always).blockVision(Blocks::always).suffocates(Blocks::always)));
SOUL_SOIL = register("soul_soil", new Block(AbstractBlock.Settings.of(Material.SOIL, MapColor.BROWN).strength(0.5F).sounds(BlockSoundGroup.SOUL_SOIL)));
BASALT = register("basalt", new PillarBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(1.25F, 4.2F).sounds(BlockSoundGroup.BASALT)));
POLISHED_BASALT = register("polished_basalt", new PillarBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(1.25F, 4.2F).sounds(BlockSoundGroup.BASALT)));
SOUL_TORCH = register("soul_torch", new TorchBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().breakInstantly().luminance((state) -> {
 return 10;
}).sounds(BlockSoundGroup.WOOD), ParticleTypes.SOUL_FIRE_FLAME));
SOUL_WALL_TORCH = register("soul_wall_torch", new WallTorchBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().breakInstantly().luminance((state) -> {
 return 10;
}).sounds(BlockSoundGroup.WOOD).dropsLike(SOUL_TORCH), ParticleTypes.SOUL_FIRE_FLAME));
GLOWSTONE = register("glowstone", new Block(AbstractBlock.Settings.of(Material.GLASS, MapColor.PALE_YELLOW).strength(0.3F).sounds(BlockSoundGroup.GLASS).luminance((state) -> {
 return 15;
})));
NETHER_PORTAL = register("nether_portal", new NetherPortalBlock(AbstractBlock.Settings.of(Material.PORTAL).noCollision().ticksRandomly().strength(-1.0F).sounds(BlockSoundGroup.GLASS).luminance((state) -> {
 return 11;
})));
CARVED_PUMPKIN = register("carved_pumpkin", new CarvedPumpkinBlock(AbstractBlock.Settings.of(Material.GOURD, MapColor.ORANGE).strength(1.0F).sounds(BlockSoundGroup.WOOD).allowsSpawning(Blocks::always)));
JACK_O_LANTERN = register("jack_o_lantern", new CarvedPumpkinBlock(AbstractBlock.Settings.of(Material.GOURD, MapColor.ORANGE).strength(1.0F).sounds(BlockSoundGroup.WOOD).luminance((state) -> {
 return 15;
}).allowsSpawning(Blocks::always)));
CAKE = register("cake", new CakeBlock(AbstractBlock.Settings.of(Material.CAKE).strength(0.5F).sounds(BlockSoundGroup.WOOL)));
REPEATER = register("repeater", new RepeaterBlock(AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().sounds(BlockSoundGroup.WOOD)));
WHITE_STAINED_GLASS = register("white_stained_glass", createStainedGlassBlock(DyeColor.WHITE));
ORANGE_STAINED_GLASS = register("orange_stained_glass", createStainedGlassBlock(DyeColor.ORANGE));
MAGENTA_STAINED_GLASS = register("magenta_stained_glass", createStainedGlassBlock(DyeColor.MAGENTA));
LIGHT_BLUE_STAINED_GLASS = register("light_blue_stained_glass", createStainedGlassBlock(DyeColor.LIGHT_BLUE));
YELLOW_STAINED_GLASS = register("yellow_stained_glass", createStainedGlassBlock(DyeColor.YELLOW));
LIME_STAINED_GLASS = register("lime_stained_glass", createStainedGlassBlock(DyeColor.LIME));
PINK_STAINED_GLASS = register("pink_stained_glass", createStainedGlassBlock(DyeColor.PINK));
GRAY_STAINED_GLASS = register("gray_stained_glass", createStainedGlassBlock(DyeColor.GRAY));
LIGHT_GRAY_STAINED_GLASS = register("light_gray_stained_glass", createStainedGlassBlock(DyeColor.LIGHT_GRAY));
CYAN_STAINED_GLASS = register("cyan_stained_glass", createStainedGlassBlock(DyeColor.CYAN));
PURPLE_STAINED_GLASS = register("purple_stained_glass", createStainedGlassBlock(DyeColor.PURPLE));
BLUE_STAINED_GLASS = register("blue_stained_glass", createStainedGlassBlock(DyeColor.BLUE));
BROWN_STAINED_GLASS = register("brown_stained_glass", createStainedGlassBlock(DyeColor.BROWN));
GREEN_STAINED_GLASS = register("green_stained_glass", createStainedGlassBlock(DyeColor.GREEN));
RED_STAINED_GLASS = register("red_stained_glass", createStainedGlassBlock(DyeColor.RED));
BLACK_STAINED_GLASS = register("black_stained_glass", createStainedGlassBlock(DyeColor.BLACK));
OAK_TRAPDOOR = register("oak_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.OAK_TAN).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
SPRUCE_TRAPDOOR = register("spruce_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.SPRUCE_BROWN).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
BIRCH_TRAPDOOR = register("birch_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.PALE_YELLOW).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
JUNGLE_TRAPDOOR = register("jungle_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.DIRT_BROWN).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
ACACIA_TRAPDOOR = register("acacia_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.ORANGE).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
DARK_OAK_TRAPDOOR = register("dark_oak_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.BROWN).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
STONE_BRICKS = register("stone_bricks", new Block(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(1.5F, 6.0F)));
MOSSY_STONE_BRICKS = register("mossy_stone_bricks", new Block(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(1.5F, 6.0F)));
CRACKED_STONE_BRICKS = register("cracked_stone_bricks", new Block(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(1.5F, 6.0F)));
CHISELED_STONE_BRICKS = register("chiseled_stone_bricks", new Block(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(1.5F, 6.0F)));
INFESTED_STONE = register("infested_stone", new InfestedBlock(STONE, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
INFESTED_COBBLESTONE = register("infested_cobblestone", new InfestedBlock(COBBLESTONE, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
INFESTED_STONE_BRICKS = register("infested_stone_bricks", new InfestedBlock(STONE_BRICKS, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
INFESTED_MOSSY_STONE_BRICKS = register("infested_mossy_stone_bricks", new InfestedBlock(MOSSY_STONE_BRICKS, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
INFESTED_CRACKED_STONE_BRICKS = register("infested_cracked_stone_bricks", new InfestedBlock(CRACKED_STONE_BRICKS, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
INFESTED_CHISELED_STONE_BRICKS = register("infested_chiseled_stone_bricks", new InfestedBlock(CHISELED_STONE_BRICKS, AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT).strength(0.0F, 0.75F)));
BROWN_MUSHROOM_BLOCK = register("brown_mushroom_block", new MushroomBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.DIRT_BROWN).strength(0.2F).sounds(BlockSoundGroup.WOOD)));
RED_MUSHROOM_BLOCK = register("red_mushroom_block", new MushroomBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.RED).strength(0.2F).sounds(BlockSoundGroup.WOOD)));
MUSHROOM_STEM = register("mushroom_stem", new MushroomBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.WHITE_GRAY).strength(0.2F).sounds(BlockSoundGroup.WOOD)));
IRON_BARS = register("iron_bars", new PaneBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.CLEAR).requiresTool().strength(5.0F, 6.0F).sounds(BlockSoundGroup.METAL).nonOpaque()));
CHAIN = register("chain", new ChainBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.CLEAR).requiresTool().strength(5.0F, 6.0F).sounds(BlockSoundGroup.CHAIN).nonOpaque()));
GLASS_PANE = register("glass_pane", new PaneBlock(AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
MELON = register("melon", new MelonBlock(AbstractBlock.Settings.of(Material.GOURD, MapColor.LIME).strength(1.0F).sounds(BlockSoundGroup.WOOD)));
ATTACHED_PUMPKIN_STEM = register("attached_pumpkin_stem", new AttachedStemBlock((GourdBlock)PUMPKIN, () -> {
 return Items.PUMPKIN_SEEDS;
}, AbstractBlock.Settings.of(Material.PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.WOOD)));
ATTACHED_MELON_STEM = register("attached_melon_stem", new AttachedStemBlock((GourdBlock)MELON, () -> {
 return Items.MELON_SEEDS;
}, AbstractBlock.Settings.of(Material.PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.WOOD)));
PUMPKIN_STEM = register("pumpkin_stem", new StemBlock((GourdBlock)PUMPKIN, () -> {
 return Items.PUMPKIN_SEEDS;
}, AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.STEM)));
MELON_STEM = register("melon_stem", new StemBlock((GourdBlock)MELON, () -> {
 return Items.MELON_SEEDS;
}, AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.STEM)));
VINE = register("vine", new VineBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().ticksRandomly().strength(0.2F).sounds(BlockSoundGroup.VINE)));
GLOW_LICHEN = register("glow_lichen", new GlowLichenBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().strength(0.2F).sounds(BlockSoundGroup.GLOW_LICHEN).luminance((blockStatex) -> {
 return 7;
})));
OAK_FENCE_GATE = register("oak_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, OAK_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
BRICK_STAIRS = register("brick_stairs", new StairsBlock(BRICKS.getDefaultState(), AbstractBlock.Settings.copy(BRICKS)));
STONE_BRICK_STAIRS = register("stone_brick_stairs", new StairsBlock(STONE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(STONE_BRICKS)));
MYCELIUM = register("mycelium", new MyceliumBlock(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.PURPLE).ticksRandomly().strength(0.6F).sounds(BlockSoundGroup.GRASS)));
LILY_PAD = register("lily_pad", new LilyPadBlock(AbstractBlock.Settings.of(Material.PLANT).breakInstantly().sounds(BlockSoundGroup.LILY_PAD).nonOpaque()));
NETHER_BRICKS = register("nether_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
NETHER_BRICK_FENCE = register("nether_brick_fence", new FenceBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
NETHER_BRICK_STAIRS = register("nether_brick_stairs", new StairsBlock(NETHER_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(NETHER_BRICKS)));
NETHER_WART = register("nether_wart", new NetherWartBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.RED).noCollision().ticksRandomly().sounds(BlockSoundGroup.NETHER_WART)));
ENCHANTING_TABLE = register("enchanting_table", new EnchantingTableBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.RED).requiresTool().strength(5.0F, 1200.0F)));
BREWING_STAND = register("brewing_stand", new BrewingStandBlock(AbstractBlock.Settings.of(Material.METAL).requiresTool().strength(0.5F).luminance((state) -> {
 return 1;
}).nonOpaque()));
CAULDRON = register("cauldron", new CauldronBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.STONE_GRAY).requiresTool().strength(2.0F).nonOpaque()));
WATER_CAULDRON = register("water_cauldron", new LeveledCauldronBlock(AbstractBlock.Settings.copy(CAULDRON), LeveledCauldronBlock.RAIN_PREDICATE, CauldronBehavior.WATER_CAULDRON_BEHAVIOR));
LAVA_CAULDRON = register("lava_cauldron", new LavaCauldronBlock(AbstractBlock.Settings.copy(CAULDRON).luminance((state) -> {
 return 15;
})));
POWDER_SNOW_CAULDRON = register("powder_snow_cauldron", new LeveledCauldronBlock(AbstractBlock.Settings.copy(CAULDRON), LeveledCauldronBlock.SNOW_PREDICATE, CauldronBehavior.POWDER_SNOW_CAULDRON_BEHAVIOR));
END_PORTAL = register("end_portal", new EndPortalBlock(AbstractBlock.Settings.of(Material.PORTAL, MapColor.BLACK).noCollision().luminance((state) -> {
 return 15;
}).strength(-1.0F, 3600000.0F).dropsNothing()));
END_PORTAL_FRAME = register("end_portal_frame", new EndPortalFrameBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GREEN).sounds(BlockSoundGroup.GLASS).luminance((state) -> {
 return 1;
}).strength(-1.0F, 3600000.0F).dropsNothing()));
END_STONE = register("end_stone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(3.0F, 9.0F)));
DRAGON_EGG = register("dragon_egg", new DragonEggBlock(AbstractBlock.Settings.of(Material.EGG, MapColor.BLACK).strength(3.0F, 9.0F).luminance((state) -> {
 return 1;
}).nonOpaque()));
REDSTONE_LAMP = register("redstone_lamp", new RedstoneLampBlock(AbstractBlock.Settings.of(Material.REDSTONE_LAMP).luminance(createLightLevelFromLitBlockState(15)).strength(0.3F).sounds(BlockSoundGroup.GLASS).allowsSpawning(Blocks::always)));
COCOA = register("cocoa", new CocoaBlock(AbstractBlock.Settings.of(Material.PLANT).ticksRandomly().strength(0.2F, 3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
SANDSTONE_STAIRS = register("sandstone_stairs", new StairsBlock(SANDSTONE.getDefaultState(), AbstractBlock.Settings.copy(SANDSTONE)));
EMERALD_ORE = register("emerald_ore", new OreBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(3.0F, 3.0F), IntRange.between(3, 7)));
ENDER_CHEST = register("ender_chest", new EnderChestBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(22.5F, 600.0F).luminance((state) -> {
 return 7;
})));
TRIPWIRE_HOOK = register("tripwire_hook", new TripwireHookBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision()));
TRIPWIRE = register("tripwire", new TripwireBlock((TripwireHookBlock)TRIPWIRE_HOOK, AbstractBlock.Settings.of(Material.DECORATION).noCollision()));
EMERALD_BLOCK = register("emerald_block", new Block(AbstractBlock.Settings.of(Material.METAL, MapColor.EMERALD_GREEN).requiresTool().strength(5.0F, 6.0F).sounds(BlockSoundGroup.METAL)));
SPRUCE_STAIRS = register("spruce_stairs", new StairsBlock(SPRUCE_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(SPRUCE_PLANKS)));
BIRCH_STAIRS = register("birch_stairs", new StairsBlock(BIRCH_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(BIRCH_PLANKS)));
JUNGLE_STAIRS = register("jungle_stairs", new StairsBlock(JUNGLE_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(JUNGLE_PLANKS)));
COMMAND_BLOCK = register("command_block", new CommandBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.BROWN).requiresTool().strength(-1.0F, 3600000.0F).dropsNothing(), false));
BEACON = register("beacon", new BeaconBlock(AbstractBlock.Settings.of(Material.GLASS, MapColor.DIAMOND_BLUE).strength(3.0F).luminance((state) -> {
 return 15;
}).nonOpaque().solidBlock(Blocks::never)));
COBBLESTONE_WALL = register("cobblestone_wall", new WallBlock(AbstractBlock.Settings.copy(COBBLESTONE)));
MOSSY_COBBLESTONE_WALL = register("mossy_cobblestone_wall", new WallBlock(AbstractBlock.Settings.copy(COBBLESTONE)));
FLOWER_POT = register("flower_pot", new FlowerPotBlock(AIR, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_OAK_SAPLING = register("potted_oak_sapling", new FlowerPotBlock(OAK_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_SPRUCE_SAPLING = register("potted_spruce_sapling", new FlowerPotBlock(SPRUCE_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_BIRCH_SAPLING = register("potted_birch_sapling", new FlowerPotBlock(BIRCH_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_JUNGLE_SAPLING = register("potted_jungle_sapling", new FlowerPotBlock(JUNGLE_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_ACACIA_SAPLING = register("potted_acacia_sapling", new FlowerPotBlock(ACACIA_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_DARK_OAK_SAPLING = register("potted_dark_oak_sapling", new FlowerPotBlock(DARK_OAK_SAPLING, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_FERN = register("potted_fern", new FlowerPotBlock(FERN, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_DANDELION = register("potted_dandelion", new FlowerPotBlock(DANDELION, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_POPPY = register("potted_poppy", new FlowerPotBlock(POPPY, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_BLUE_ORCHID = register("potted_blue_orchid", new FlowerPotBlock(BLUE_ORCHID, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_ALLIUM = register("potted_allium", new FlowerPotBlock(ALLIUM, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_AZURE_BLUET = register("potted_azure_bluet", new FlowerPotBlock(AZURE_BLUET, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_RED_TULIP = register("potted_red_tulip", new FlowerPotBlock(RED_TULIP, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_ORANGE_TULIP = register("potted_orange_tulip", new FlowerPotBlock(ORANGE_TULIP, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_WHITE_TULIP = register("potted_white_tulip", new FlowerPotBlock(WHITE_TULIP, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_PINK_TULIP = register("potted_pink_tulip", new FlowerPotBlock(PINK_TULIP, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_OXEYE_DAISY = register("potted_oxeye_daisy", new FlowerPotBlock(OXEYE_DAISY, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_CORNFLOWER = register("potted_cornflower", new FlowerPotBlock(CORNFLOWER, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_LILY_OF_THE_VALLEY = register("potted_lily_of_the_valley", new FlowerPotBlock(LILY_OF_THE_VALLEY, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_WITHER_ROSE = register("potted_wither_rose", new FlowerPotBlock(WITHER_ROSE, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_RED_MUSHROOM = register("potted_red_mushroom", new FlowerPotBlock(RED_MUSHROOM, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_BROWN_MUSHROOM = register("potted_brown_mushroom", new FlowerPotBlock(BROWN_MUSHROOM, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_DEAD_BUSH = register("potted_dead_bush", new FlowerPotBlock(DEAD_BUSH, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_CACTUS = register("potted_cactus", new FlowerPotBlock(CACTUS, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
CARROTS = register("carrots", new CarrotsBlock(AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.CROP)));
POTATOES = register("potatoes", new PotatoesBlock(AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.CROP)));
OAK_BUTTON = register("oak_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
SPRUCE_BUTTON = register("spruce_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
BIRCH_BUTTON = register("birch_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
JUNGLE_BUTTON = register("jungle_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
ACACIA_BUTTON = register("acacia_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
DARK_OAK_BUTTON = register("dark_oak_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
SKELETON_SKULL = register("skeleton_skull", new SkullBlock(SkullBlock.Type.SKELETON, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
SKELETON_WALL_SKULL = register("skeleton_wall_skull", new WallSkullBlock(SkullBlock.Type.SKELETON, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(SKELETON_SKULL)));
WITHER_SKELETON_SKULL = register("wither_skeleton_skull", new WitherSkullBlock(AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
WITHER_SKELETON_WALL_SKULL = register("wither_skeleton_wall_skull", new WallWitherSkullBlock(AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(WITHER_SKELETON_SKULL)));
ZOMBIE_HEAD = register("zombie_head", new SkullBlock(SkullBlock.Type.ZOMBIE, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
ZOMBIE_WALL_HEAD = register("zombie_wall_head", new WallSkullBlock(SkullBlock.Type.ZOMBIE, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(ZOMBIE_HEAD)));
PLAYER_HEAD = register("player_head", new PlayerSkullBlock(AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
PLAYER_WALL_HEAD = register("player_wall_head", new WallPlayerSkullBlock(AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(PLAYER_HEAD)));
CREEPER_HEAD = register("creeper_head", new SkullBlock(SkullBlock.Type.CREEPER, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
CREEPER_WALL_HEAD = register("creeper_wall_head", new WallSkullBlock(SkullBlock.Type.CREEPER, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(CREEPER_HEAD)));
DRAGON_HEAD = register("dragon_head", new SkullBlock(SkullBlock.Type.DRAGON, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F)));
DRAGON_WALL_HEAD = register("dragon_wall_head", new WallSkullBlock(SkullBlock.Type.DRAGON, AbstractBlock.Settings.of(Material.DECORATION).strength(1.0F).dropsLike(DRAGON_HEAD)));
ANVIL = register("anvil", new AnvilBlock(AbstractBlock.Settings.of(Material.REPAIR_STATION, MapColor.IRON_GRAY).requiresTool().strength(5.0F, 1200.0F).sounds(BlockSoundGroup.ANVIL)));
CHIPPED_ANVIL = register("chipped_anvil", new AnvilBlock(AbstractBlock.Settings.of(Material.REPAIR_STATION, MapColor.IRON_GRAY).requiresTool().strength(5.0F, 1200.0F).sounds(BlockSoundGroup.ANVIL)));
DAMAGED_ANVIL = register("damaged_anvil", new AnvilBlock(AbstractBlock.Settings.of(Material.REPAIR_STATION, MapColor.IRON_GRAY).requiresTool().strength(5.0F, 1200.0F).sounds(BlockSoundGroup.ANVIL)));
TRAPPED_CHEST = register("trapped_chest", new TrappedChestBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
LIGHT_WEIGHTED_PRESSURE_PLATE = register("light_weighted_pressure_plate", new WeightedPressurePlateBlock(15, AbstractBlock.Settings.of(Material.METAL, MapColor.GOLD).requiresTool().noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
HEAVY_WEIGHTED_PRESSURE_PLATE = register("heavy_weighted_pressure_plate", new WeightedPressurePlateBlock(150, AbstractBlock.Settings.of(Material.METAL).requiresTool().noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
COMPARATOR = register("comparator", new ComparatorBlock(AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().sounds(BlockSoundGroup.WOOD)));
DAYLIGHT_DETECTOR = register("daylight_detector", new DaylightDetectorBlock(AbstractBlock.Settings.of(Material.WOOD).strength(0.2F).sounds(BlockSoundGroup.WOOD)));
REDSTONE_BLOCK = register("redstone_block", new RedstoneBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.BRIGHT_RED).requiresTool().strength(5.0F, 6.0F).sounds(BlockSoundGroup.METAL).solidBlock(Blocks::never)));
NETHER_QUARTZ_ORE = register("nether_quartz_ore", new OreBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(3.0F, 3.0F).sounds(BlockSoundGroup.NETHER_ORE), IntRange.between(2, 5)));
HOPPER = register("hopper", new HopperBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.STONE_GRAY).requiresTool().strength(3.0F, 4.8F).sounds(BlockSoundGroup.METAL).nonOpaque()));
QUARTZ_BLOCK = register("quartz_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.OFF_WHITE).requiresTool().strength(0.8F)));
CHISELED_QUARTZ_BLOCK = register("chiseled_quartz_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.OFF_WHITE).requiresTool().strength(0.8F)));
QUARTZ_PILLAR = register("quartz_pillar", new PillarBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.OFF_WHITE).requiresTool().strength(0.8F)));
QUARTZ_STAIRS = register("quartz_stairs", new StairsBlock(QUARTZ_BLOCK.getDefaultState(), AbstractBlock.Settings.copy(QUARTZ_BLOCK)));
ACTIVATOR_RAIL = register("activator_rail", new PoweredRailBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.7F).sounds(BlockSoundGroup.METAL)));
DROPPER = register("dropper", new DropperBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(3.5F)));
WHITE_TERRACOTTA = register("white_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_WHITE).requiresTool().strength(1.25F, 4.2F)));
ORANGE_TERRACOTTA = register("orange_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_ORANGE).requiresTool().strength(1.25F, 4.2F)));
MAGENTA_TERRACOTTA = register("magenta_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_MAGENTA).requiresTool().strength(1.25F, 4.2F)));
LIGHT_BLUE_TERRACOTTA = register("light_blue_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_LIGHT_BLUE).requiresTool().strength(1.25F, 4.2F)));
YELLOW_TERRACOTTA = register("yellow_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_YELLOW).requiresTool().strength(1.25F, 4.2F)));
LIME_TERRACOTTA = register("lime_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_LIME).requiresTool().strength(1.25F, 4.2F)));
PINK_TERRACOTTA = register("pink_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_PINK).requiresTool().strength(1.25F, 4.2F)));
GRAY_TERRACOTTA = register("gray_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_GRAY).requiresTool().strength(1.25F, 4.2F)));
LIGHT_GRAY_TERRACOTTA = register("light_gray_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_LIGHT_GRAY).requiresTool().strength(1.25F, 4.2F)));
CYAN_TERRACOTTA = register("cyan_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_CYAN).requiresTool().strength(1.25F, 4.2F)));
PURPLE_TERRACOTTA = register("purple_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_PURPLE).requiresTool().strength(1.25F, 4.2F)));
BLUE_TERRACOTTA = register("blue_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_BLUE).requiresTool().strength(1.25F, 4.2F)));
BROWN_TERRACOTTA = register("brown_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_BROWN).requiresTool().strength(1.25F, 4.2F)));
GREEN_TERRACOTTA = register("green_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_GREEN).requiresTool().strength(1.25F, 4.2F)));
RED_TERRACOTTA = register("red_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_RED).requiresTool().strength(1.25F, 4.2F)));
BLACK_TERRACOTTA = register("black_terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_BLACK).requiresTool().strength(1.25F, 4.2F)));
WHITE_STAINED_GLASS_PANE = register("white_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.WHITE, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
ORANGE_STAINED_GLASS_PANE = register("orange_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.ORANGE, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
MAGENTA_STAINED_GLASS_PANE = register("magenta_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.MAGENTA, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
LIGHT_BLUE_STAINED_GLASS_PANE = register("light_blue_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.LIGHT_BLUE, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
YELLOW_STAINED_GLASS_PANE = register("yellow_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.YELLOW, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
LIME_STAINED_GLASS_PANE = register("lime_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.LIME, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
PINK_STAINED_GLASS_PANE = register("pink_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.PINK, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
GRAY_STAINED_GLASS_PANE = register("gray_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.GRAY, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
LIGHT_GRAY_STAINED_GLASS_PANE = register("light_gray_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.LIGHT_GRAY, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
CYAN_STAINED_GLASS_PANE = register("cyan_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.CYAN, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
PURPLE_STAINED_GLASS_PANE = register("purple_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.PURPLE, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
BLUE_STAINED_GLASS_PANE = register("blue_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.BLUE, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
BROWN_STAINED_GLASS_PANE = register("brown_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.BROWN, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
GREEN_STAINED_GLASS_PANE = register("green_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.GREEN, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
RED_STAINED_GLASS_PANE = register("red_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.RED, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
BLACK_STAINED_GLASS_PANE = register("black_stained_glass_pane", new StainedGlassPaneBlock(DyeColor.BLACK, AbstractBlock.Settings.of(Material.GLASS).strength(0.3F).sounds(BlockSoundGroup.GLASS).nonOpaque()));
ACACIA_STAIRS = register("acacia_stairs", new StairsBlock(ACACIA_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(ACACIA_PLANKS)));
DARK_OAK_STAIRS = register("dark_oak_stairs", new StairsBlock(DARK_OAK_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(DARK_OAK_PLANKS)));
SLIME_BLOCK = register("slime_block", new SlimeBlock(AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT, MapColor.PALE_GREEN).slipperiness(0.8F).sounds(BlockSoundGroup.SLIME).nonOpaque()));
BARRIER = register("barrier", new BarrierBlock(AbstractBlock.Settings.of(Material.BARRIER).strength(-1.0F, 3600000.8F).dropsNothing().nonOpaque().allowsSpawning(Blocks::never)));
IRON_TRAPDOOR = register("iron_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.METAL).requiresTool().strength(5.0F).sounds(BlockSoundGroup.METAL).nonOpaque().allowsSpawning(Blocks::never)));
PRISMARINE = register("prismarine", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.CYAN).requiresTool().strength(1.5F, 6.0F)));
PRISMARINE_BRICKS = register("prismarine_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DIAMOND_BLUE).requiresTool().strength(1.5F, 6.0F)));
DARK_PRISMARINE = register("dark_prismarine", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DIAMOND_BLUE).requiresTool().strength(1.5F, 6.0F)));
PRISMARINE_STAIRS = register("prismarine_stairs", new StairsBlock(PRISMARINE.getDefaultState(), AbstractBlock.Settings.copy(PRISMARINE)));
PRISMARINE_BRICK_STAIRS = register("prismarine_brick_stairs", new StairsBlock(PRISMARINE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(PRISMARINE_BRICKS)));
DARK_PRISMARINE_STAIRS = register("dark_prismarine_stairs", new StairsBlock(DARK_PRISMARINE.getDefaultState(), AbstractBlock.Settings.copy(DARK_PRISMARINE)));
PRISMARINE_SLAB = register("prismarine_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.CYAN).requiresTool().strength(1.5F, 6.0F)));
PRISMARINE_BRICK_SLAB = register("prismarine_brick_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DIAMOND_BLUE).requiresTool().strength(1.5F, 6.0F)));
DARK_PRISMARINE_SLAB = register("dark_prismarine_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DIAMOND_BLUE).requiresTool().strength(1.5F, 6.0F)));
SEA_LANTERN = register("sea_lantern", new Block(AbstractBlock.Settings.of(Material.GLASS, MapColor.OFF_WHITE).strength(0.3F).sounds(BlockSoundGroup.GLASS).luminance((state) -> {
 return 15;
})));
HAY_BLOCK = register("hay_block", new HayBlock(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.YELLOW).strength(0.5F).sounds(BlockSoundGroup.GRASS)));
WHITE_CARPET = register("white_carpet", new DyedCarpetBlock(DyeColor.WHITE, AbstractBlock.Settings.of(Material.CARPET, MapColor.WHITE).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
ORANGE_CARPET = register("orange_carpet", new DyedCarpetBlock(DyeColor.ORANGE, AbstractBlock.Settings.of(Material.CARPET, MapColor.ORANGE).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
MAGENTA_CARPET = register("magenta_carpet", new DyedCarpetBlock(DyeColor.MAGENTA, AbstractBlock.Settings.of(Material.CARPET, MapColor.MAGENTA).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
LIGHT_BLUE_CARPET = register("light_blue_carpet", new DyedCarpetBlock(DyeColor.LIGHT_BLUE, AbstractBlock.Settings.of(Material.CARPET, MapColor.LIGHT_BLUE).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
YELLOW_CARPET = register("yellow_carpet", new DyedCarpetBlock(DyeColor.YELLOW, AbstractBlock.Settings.of(Material.CARPET, MapColor.YELLOW).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
LIME_CARPET = register("lime_carpet", new DyedCarpetBlock(DyeColor.LIME, AbstractBlock.Settings.of(Material.CARPET, MapColor.LIME).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
PINK_CARPET = register("pink_carpet", new DyedCarpetBlock(DyeColor.PINK, AbstractBlock.Settings.of(Material.CARPET, MapColor.PINK).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
GRAY_CARPET = register("gray_carpet", new DyedCarpetBlock(DyeColor.GRAY, AbstractBlock.Settings.of(Material.CARPET, MapColor.GRAY).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
LIGHT_GRAY_CARPET = register("light_gray_carpet", new DyedCarpetBlock(DyeColor.LIGHT_GRAY, AbstractBlock.Settings.of(Material.CARPET, MapColor.LIGHT_GRAY).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
CYAN_CARPET = register("cyan_carpet", new DyedCarpetBlock(DyeColor.CYAN, AbstractBlock.Settings.of(Material.CARPET, MapColor.CYAN).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
PURPLE_CARPET = register("purple_carpet", new DyedCarpetBlock(DyeColor.PURPLE, AbstractBlock.Settings.of(Material.CARPET, MapColor.PURPLE).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
BLUE_CARPET = register("blue_carpet", new DyedCarpetBlock(DyeColor.BLUE, AbstractBlock.Settings.of(Material.CARPET, MapColor.BLUE).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
BROWN_CARPET = register("brown_carpet", new DyedCarpetBlock(DyeColor.BROWN, AbstractBlock.Settings.of(Material.CARPET, MapColor.BROWN).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
GREEN_CARPET = register("green_carpet", new DyedCarpetBlock(DyeColor.GREEN, AbstractBlock.Settings.of(Material.CARPET, MapColor.GREEN).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
RED_CARPET = register("red_carpet", new DyedCarpetBlock(DyeColor.RED, AbstractBlock.Settings.of(Material.CARPET, MapColor.RED).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
BLACK_CARPET = register("black_carpet", new DyedCarpetBlock(DyeColor.BLACK, AbstractBlock.Settings.of(Material.CARPET, MapColor.BLACK).strength(0.1F).sounds(BlockSoundGroup.WOOL)));
TERRACOTTA = register("terracotta", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(1.25F, 4.2F)));
COAL_BLOCK = register("coal_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(5.0F, 6.0F)));
PACKED_ICE = register("packed_ice", new Block(AbstractBlock.Settings.of(Material.DENSE_ICE).slipperiness(0.98F).strength(0.5F).sounds(BlockSoundGroup.GLASS)));
SUNFLOWER = register("sunflower", new TallFlowerBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
LILAC = register("lilac", new TallFlowerBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
ROSE_BUSH = register("rose_bush", new TallFlowerBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
PEONY = register("peony", new TallFlowerBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
TALL_GRASS = register("tall_grass", new TallPlantBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
LARGE_FERN = register("large_fern", new TallPlantBlock(AbstractBlock.Settings.of(Material.REPLACEABLE_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.GRASS)));
WHITE_BANNER = register("white_banner", new BannerBlock(DyeColor.WHITE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
ORANGE_BANNER = register("orange_banner", new BannerBlock(DyeColor.ORANGE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
MAGENTA_BANNER = register("magenta_banner", new BannerBlock(DyeColor.MAGENTA, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
LIGHT_BLUE_BANNER = register("light_blue_banner", new BannerBlock(DyeColor.LIGHT_BLUE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
YELLOW_BANNER = register("yellow_banner", new BannerBlock(DyeColor.YELLOW, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
LIME_BANNER = register("lime_banner", new BannerBlock(DyeColor.LIME, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
PINK_BANNER = register("pink_banner", new BannerBlock(DyeColor.PINK, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
GRAY_BANNER = register("gray_banner", new BannerBlock(DyeColor.GRAY, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
LIGHT_GRAY_BANNER = register("light_gray_banner", new BannerBlock(DyeColor.LIGHT_GRAY, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
CYAN_BANNER = register("cyan_banner", new BannerBlock(DyeColor.CYAN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
PURPLE_BANNER = register("purple_banner", new BannerBlock(DyeColor.PURPLE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
BLUE_BANNER = register("blue_banner", new BannerBlock(DyeColor.BLUE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
BROWN_BANNER = register("brown_banner", new BannerBlock(DyeColor.BROWN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
GREEN_BANNER = register("green_banner", new BannerBlock(DyeColor.GREEN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
RED_BANNER = register("red_banner", new BannerBlock(DyeColor.RED, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
BLACK_BANNER = register("black_banner", new BannerBlock(DyeColor.BLACK, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD)));
WHITE_WALL_BANNER = register("white_wall_banner", new WallBannerBlock(DyeColor.WHITE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(WHITE_BANNER)));
ORANGE_WALL_BANNER = register("orange_wall_banner", new WallBannerBlock(DyeColor.ORANGE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(ORANGE_BANNER)));
MAGENTA_WALL_BANNER = register("magenta_wall_banner", new WallBannerBlock(DyeColor.MAGENTA, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(MAGENTA_BANNER)));
LIGHT_BLUE_WALL_BANNER = register("light_blue_wall_banner", new WallBannerBlock(DyeColor.LIGHT_BLUE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(LIGHT_BLUE_BANNER)));
YELLOW_WALL_BANNER = register("yellow_wall_banner", new WallBannerBlock(DyeColor.YELLOW, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(YELLOW_BANNER)));
LIME_WALL_BANNER = register("lime_wall_banner", new WallBannerBlock(DyeColor.LIME, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(LIME_BANNER)));
PINK_WALL_BANNER = register("pink_wall_banner", new WallBannerBlock(DyeColor.PINK, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(PINK_BANNER)));
GRAY_WALL_BANNER = register("gray_wall_banner", new WallBannerBlock(DyeColor.GRAY, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(GRAY_BANNER)));
LIGHT_GRAY_WALL_BANNER = register("light_gray_wall_banner", new WallBannerBlock(DyeColor.LIGHT_GRAY, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(LIGHT_GRAY_BANNER)));
CYAN_WALL_BANNER = register("cyan_wall_banner", new WallBannerBlock(DyeColor.CYAN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(CYAN_BANNER)));
PURPLE_WALL_BANNER = register("purple_wall_banner", new WallBannerBlock(DyeColor.PURPLE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(PURPLE_BANNER)));
BLUE_WALL_BANNER = register("blue_wall_banner", new WallBannerBlock(DyeColor.BLUE, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(BLUE_BANNER)));
BROWN_WALL_BANNER = register("brown_wall_banner", new WallBannerBlock(DyeColor.BROWN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(BROWN_BANNER)));
GREEN_WALL_BANNER = register("green_wall_banner", new WallBannerBlock(DyeColor.GREEN, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(GREEN_BANNER)));
RED_WALL_BANNER = register("red_wall_banner", new WallBannerBlock(DyeColor.RED, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(RED_BANNER)));
BLACK_WALL_BANNER = register("black_wall_banner", new WallBannerBlock(DyeColor.BLACK, AbstractBlock.Settings.of(Material.WOOD).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(BLACK_BANNER)));
RED_SANDSTONE = register("red_sandstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(0.8F)));
CHISELED_RED_SANDSTONE = register("chiseled_red_sandstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(0.8F)));
CUT_RED_SANDSTONE = register("cut_red_sandstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(0.8F)));
RED_SANDSTONE_STAIRS = register("red_sandstone_stairs", new StairsBlock(RED_SANDSTONE.getDefaultState(), AbstractBlock.Settings.copy(RED_SANDSTONE)));
OAK_SLAB = register("oak_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.OAK_TAN).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
SPRUCE_SLAB = register("spruce_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.SPRUCE_BROWN).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
BIRCH_SLAB = register("birch_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.PALE_YELLOW).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
JUNGLE_SLAB = register("jungle_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.DIRT_BROWN).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
ACACIA_SLAB = register("acacia_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.ORANGE).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
DARK_OAK_SLAB = register("dark_oak_slab", new SlabBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.BROWN).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
STONE_SLAB = register("stone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(2.0F, 6.0F)));
SMOOTH_STONE_SLAB = register("smooth_stone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(2.0F, 6.0F)));
SANDSTONE_SLAB = register("sandstone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(2.0F, 6.0F)));
CUT_SANDSTONE_SLAB = register("cut_sandstone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(2.0F, 6.0F)));
PETRIFIED_OAK_SLAB = register("petrified_oak_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.OAK_TAN).requiresTool().strength(2.0F, 6.0F)));
COBBLESTONE_SLAB = register("cobblestone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(2.0F, 6.0F)));
BRICK_SLAB = register("brick_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.RED).requiresTool().strength(2.0F, 6.0F)));
STONE_BRICK_SLAB = register("stone_brick_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(2.0F, 6.0F)));
NETHER_BRICK_SLAB = register("nether_brick_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
QUARTZ_SLAB = register("quartz_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.OFF_WHITE).requiresTool().strength(2.0F, 6.0F)));
RED_SANDSTONE_SLAB = register("red_sandstone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(2.0F, 6.0F)));
CUT_RED_SANDSTONE_SLAB = register("cut_red_sandstone_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(2.0F, 6.0F)));
PURPUR_SLAB = register("purpur_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.MAGENTA).requiresTool().strength(2.0F, 6.0F)));
SMOOTH_STONE = register("smooth_stone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(2.0F, 6.0F)));
SMOOTH_SANDSTONE = register("smooth_sandstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(2.0F, 6.0F)));
SMOOTH_QUARTZ = register("smooth_quartz", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.OFF_WHITE).requiresTool().strength(2.0F, 6.0F)));
SMOOTH_RED_SANDSTONE = register("smooth_red_sandstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.ORANGE).requiresTool().strength(2.0F, 6.0F)));
SPRUCE_FENCE_GATE = register("spruce_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, SPRUCE_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
BIRCH_FENCE_GATE = register("birch_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, BIRCH_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
JUNGLE_FENCE_GATE = register("jungle_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, JUNGLE_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
ACACIA_FENCE_GATE = register("acacia_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, ACACIA_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
DARK_OAK_FENCE_GATE = register("dark_oak_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
SPRUCE_FENCE = register("spruce_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, SPRUCE_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
BIRCH_FENCE = register("birch_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, BIRCH_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
JUNGLE_FENCE = register("jungle_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, JUNGLE_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
ACACIA_FENCE = register("acacia_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, ACACIA_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
DARK_OAK_FENCE = register("dark_oak_fence", new FenceBlock(AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
SPRUCE_DOOR = register("spruce_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, SPRUCE_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
BIRCH_DOOR = register("birch_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, BIRCH_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
JUNGLE_DOOR = register("jungle_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, JUNGLE_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
ACACIA_DOOR = register("acacia_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, ACACIA_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
DARK_OAK_DOOR = register("dark_oak_door", new DoorBlock(AbstractBlock.Settings.of(Material.WOOD, DARK_OAK_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
END_ROD = register("end_rod", new EndRodBlock(AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().luminance((state) -> {
 return 14;
}).sounds(BlockSoundGroup.WOOD).nonOpaque()));
CHORUS_PLANT = register("chorus_plant", new ChorusPlantBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.PURPLE).strength(0.4F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
CHORUS_FLOWER = register("chorus_flower", new ChorusFlowerBlock((ChorusPlantBlock)CHORUS_PLANT, AbstractBlock.Settings.of(Material.PLANT, MapColor.PURPLE).ticksRandomly().strength(0.4F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
PURPUR_BLOCK = register("purpur_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.MAGENTA).requiresTool().strength(1.5F, 6.0F)));
PURPUR_PILLAR = register("purpur_pillar", new PillarBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.MAGENTA).requiresTool().strength(1.5F, 6.0F)));
PURPUR_STAIRS = register("purpur_stairs", new StairsBlock(PURPUR_BLOCK.getDefaultState(), AbstractBlock.Settings.copy(PURPUR_BLOCK)));
END_STONE_BRICKS = register("end_stone_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(3.0F, 9.0F)));
BEETROOTS = register("beetroots", new BeetrootsBlock(AbstractBlock.Settings.of(Material.PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.CROP)));
DIRT_PATH = register("dirt_path", new DirtPathBlock(AbstractBlock.Settings.of(Material.SOIL).strength(0.65F).sounds(BlockSoundGroup.GRASS).blockVision(Blocks::always).suffocates(Blocks::always)));
END_GATEWAY = register("end_gateway", new EndGatewayBlock(AbstractBlock.Settings.of(Material.PORTAL, MapColor.BLACK).noCollision().luminance((state) -> {
 return 15;
}).strength(-1.0F, 3600000.0F).dropsNothing()));
REPEATING_COMMAND_BLOCK = register("repeating_command_block", new CommandBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.PURPLE).requiresTool().strength(-1.0F, 3600000.0F).dropsNothing(), false));
CHAIN_COMMAND_BLOCK = register("chain_command_block", new CommandBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.GREEN).requiresTool().strength(-1.0F, 3600000.0F).dropsNothing(), true));
FROSTED_ICE = register("frosted_ice", new FrostedIceBlock(AbstractBlock.Settings.of(Material.ICE).slipperiness(0.98F).ticksRandomly().strength(0.5F).sounds(BlockSoundGroup.GLASS).nonOpaque().allowsSpawning((state, world, pos, entityType) -> {
 return entityType == EntityType.POLAR_BEAR;
})));
MAGMA_BLOCK = register("magma_block", new MagmaBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().luminance((state) -> {
 return 3;
}).ticksRandomly().strength(0.5F).allowsSpawning((state, world, pos, entityType) -> {
 return entityType.isFireImmune();
}).postProcess(Blocks::always).emissiveLighting(Blocks::always)));
NETHER_WART_BLOCK = register("nether_wart_block", new Block(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.RED).strength(1.0F).sounds(BlockSoundGroup.WART_BLOCK)));
RED_NETHER_BRICKS = register("red_nether_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
BONE_BLOCK = register("bone_block", new PillarBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.PALE_YELLOW).requiresTool().strength(2.0F).sounds(BlockSoundGroup.BONE)));
STRUCTURE_VOID = register("structure_void", new StructureVoidBlock(AbstractBlock.Settings.of(Material.STRUCTURE_VOID).noCollision().dropsNothing()));
OBSERVER = register("observer", new ObserverBlock(AbstractBlock.Settings.of(Material.STONE).strength(3.0F).requiresTool().solidBlock(Blocks::never)));
SHULKER_BOX = register("shulker_box", createShulkerBoxBlock((DyeColor)null, AbstractBlock.Settings.of(Material.SHULKER_BOX)));
WHITE_SHULKER_BOX = register("white_shulker_box", createShulkerBoxBlock(DyeColor.WHITE, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.WHITE)));
ORANGE_SHULKER_BOX = register("orange_shulker_box", createShulkerBoxBlock(DyeColor.ORANGE, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.ORANGE)));
MAGENTA_SHULKER_BOX = register("magenta_shulker_box", createShulkerBoxBlock(DyeColor.MAGENTA, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.MAGENTA)));
LIGHT_BLUE_SHULKER_BOX = register("light_blue_shulker_box", createShulkerBoxBlock(DyeColor.LIGHT_BLUE, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.LIGHT_BLUE)));
YELLOW_SHULKER_BOX = register("yellow_shulker_box", createShulkerBoxBlock(DyeColor.YELLOW, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.YELLOW)));
LIME_SHULKER_BOX = register("lime_shulker_box", createShulkerBoxBlock(DyeColor.LIME, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.LIME)));
PINK_SHULKER_BOX = register("pink_shulker_box", createShulkerBoxBlock(DyeColor.PINK, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.PINK)));
GRAY_SHULKER_BOX = register("gray_shulker_box", createShulkerBoxBlock(DyeColor.GRAY, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.GRAY)));
LIGHT_GRAY_SHULKER_BOX = register("light_gray_shulker_box", createShulkerBoxBlock(DyeColor.LIGHT_GRAY, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.LIGHT_GRAY)));
CYAN_SHULKER_BOX = register("cyan_shulker_box", createShulkerBoxBlock(DyeColor.CYAN, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.CYAN)));
PURPLE_SHULKER_BOX = register("purple_shulker_box", createShulkerBoxBlock(DyeColor.PURPLE, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.TERRACOTTA_PURPLE)));
BLUE_SHULKER_BOX = register("blue_shulker_box", createShulkerBoxBlock(DyeColor.BLUE, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.BLUE)));
BROWN_SHULKER_BOX = register("brown_shulker_box", createShulkerBoxBlock(DyeColor.BROWN, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.BROWN)));
GREEN_SHULKER_BOX = register("green_shulker_box", createShulkerBoxBlock(DyeColor.GREEN, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.GREEN)));
RED_SHULKER_BOX = register("red_shulker_box", createShulkerBoxBlock(DyeColor.RED, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.RED)));
BLACK_SHULKER_BOX = register("black_shulker_box", createShulkerBoxBlock(DyeColor.BLACK, AbstractBlock.Settings.of(Material.SHULKER_BOX, MapColor.BLACK)));
WHITE_GLAZED_TERRACOTTA = register("white_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.WHITE).requiresTool().strength(1.4F)));
ORANGE_GLAZED_TERRACOTTA = register("orange_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.ORANGE).requiresTool().strength(1.4F)));
MAGENTA_GLAZED_TERRACOTTA = register("magenta_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.MAGENTA).requiresTool().strength(1.4F)));
LIGHT_BLUE_GLAZED_TERRACOTTA = register("light_blue_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIGHT_BLUE).requiresTool().strength(1.4F)));
YELLOW_GLAZED_TERRACOTTA = register("yellow_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.YELLOW).requiresTool().strength(1.4F)));
LIME_GLAZED_TERRACOTTA = register("lime_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIME).requiresTool().strength(1.4F)));
PINK_GLAZED_TERRACOTTA = register("pink_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.PINK).requiresTool().strength(1.4F)));
GRAY_GLAZED_TERRACOTTA = register("gray_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.GRAY).requiresTool().strength(1.4F)));
LIGHT_GRAY_GLAZED_TERRACOTTA = register("light_gray_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIGHT_GRAY).requiresTool().strength(1.4F)));
CYAN_GLAZED_TERRACOTTA = register("cyan_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.CYAN).requiresTool().strength(1.4F)));
PURPLE_GLAZED_TERRACOTTA = register("purple_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.PURPLE).requiresTool().strength(1.4F)));
BLUE_GLAZED_TERRACOTTA = register("blue_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.BLUE).requiresTool().strength(1.4F)));
BROWN_GLAZED_TERRACOTTA = register("brown_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.BROWN).requiresTool().strength(1.4F)));
GREEN_GLAZED_TERRACOTTA = register("green_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.GREEN).requiresTool().strength(1.4F)));
RED_GLAZED_TERRACOTTA = register("red_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.RED).requiresTool().strength(1.4F)));
BLACK_GLAZED_TERRACOTTA = register("black_glazed_terracotta", new GlazedTerracottaBlock(AbstractBlock.Settings.of(Material.STONE, DyeColor.BLACK).requiresTool().strength(1.4F)));
WHITE_CONCRETE = register("white_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.WHITE).requiresTool().strength(1.8F)));
ORANGE_CONCRETE = register("orange_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.ORANGE).requiresTool().strength(1.8F)));
MAGENTA_CONCRETE = register("magenta_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.MAGENTA).requiresTool().strength(1.8F)));
LIGHT_BLUE_CONCRETE = register("light_blue_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIGHT_BLUE).requiresTool().strength(1.8F)));
YELLOW_CONCRETE = register("yellow_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.YELLOW).requiresTool().strength(1.8F)));
LIME_CONCRETE = register("lime_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIME).requiresTool().strength(1.8F)));
PINK_CONCRETE = register("pink_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.PINK).requiresTool().strength(1.8F)));
GRAY_CONCRETE = register("gray_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.GRAY).requiresTool().strength(1.8F)));
LIGHT_GRAY_CONCRETE = register("light_gray_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.LIGHT_GRAY).requiresTool().strength(1.8F)));
CYAN_CONCRETE = register("cyan_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.CYAN).requiresTool().strength(1.8F)));
PURPLE_CONCRETE = register("purple_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.PURPLE).requiresTool().strength(1.8F)));
BLUE_CONCRETE = register("blue_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.BLUE).requiresTool().strength(1.8F)));
BROWN_CONCRETE = register("brown_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.BROWN).requiresTool().strength(1.8F)));
GREEN_CONCRETE = register("green_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.GREEN).requiresTool().strength(1.8F)));
RED_CONCRETE = register("red_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.RED).requiresTool().strength(1.8F)));
BLACK_CONCRETE = register("black_concrete", new Block(AbstractBlock.Settings.of(Material.STONE, DyeColor.BLACK).requiresTool().strength(1.8F)));
WHITE_CONCRETE_POWDER = register("white_concrete_powder", new ConcretePowderBlock(WHITE_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.WHITE).strength(0.5F).sounds(BlockSoundGroup.SAND)));
ORANGE_CONCRETE_POWDER = register("orange_concrete_powder", new ConcretePowderBlock(ORANGE_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.ORANGE).strength(0.5F).sounds(BlockSoundGroup.SAND)));
MAGENTA_CONCRETE_POWDER = register("magenta_concrete_powder", new ConcretePowderBlock(MAGENTA_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.MAGENTA).strength(0.5F).sounds(BlockSoundGroup.SAND)));
LIGHT_BLUE_CONCRETE_POWDER = register("light_blue_concrete_powder", new ConcretePowderBlock(LIGHT_BLUE_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.LIGHT_BLUE).strength(0.5F).sounds(BlockSoundGroup.SAND)));
YELLOW_CONCRETE_POWDER = register("yellow_concrete_powder", new ConcretePowderBlock(YELLOW_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.YELLOW).strength(0.5F).sounds(BlockSoundGroup.SAND)));
LIME_CONCRETE_POWDER = register("lime_concrete_powder", new ConcretePowderBlock(LIME_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.LIME).strength(0.5F).sounds(BlockSoundGroup.SAND)));
PINK_CONCRETE_POWDER = register("pink_concrete_powder", new ConcretePowderBlock(PINK_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.PINK).strength(0.5F).sounds(BlockSoundGroup.SAND)));
GRAY_CONCRETE_POWDER = register("gray_concrete_powder", new ConcretePowderBlock(GRAY_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.GRAY).strength(0.5F).sounds(BlockSoundGroup.SAND)));
LIGHT_GRAY_CONCRETE_POWDER = register("light_gray_concrete_powder", new ConcretePowderBlock(LIGHT_GRAY_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.LIGHT_GRAY).strength(0.5F).sounds(BlockSoundGroup.SAND)));
CYAN_CONCRETE_POWDER = register("cyan_concrete_powder", new ConcretePowderBlock(CYAN_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.CYAN).strength(0.5F).sounds(BlockSoundGroup.SAND)));
PURPLE_CONCRETE_POWDER = register("purple_concrete_powder", new ConcretePowderBlock(PURPLE_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.PURPLE).strength(0.5F).sounds(BlockSoundGroup.SAND)));
BLUE_CONCRETE_POWDER = register("blue_concrete_powder", new ConcretePowderBlock(BLUE_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.BLUE).strength(0.5F).sounds(BlockSoundGroup.SAND)));
BROWN_CONCRETE_POWDER = register("brown_concrete_powder", new ConcretePowderBlock(BROWN_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.BROWN).strength(0.5F).sounds(BlockSoundGroup.SAND)));
GREEN_CONCRETE_POWDER = register("green_concrete_powder", new ConcretePowderBlock(GREEN_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.GREEN).strength(0.5F).sounds(BlockSoundGroup.SAND)));
RED_CONCRETE_POWDER = register("red_concrete_powder", new ConcretePowderBlock(RED_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.RED).strength(0.5F).sounds(BlockSoundGroup.SAND)));
BLACK_CONCRETE_POWDER = register("black_concrete_powder", new ConcretePowderBlock(BLACK_CONCRETE, AbstractBlock.Settings.of(Material.AGGREGATE, DyeColor.BLACK).strength(0.5F).sounds(BlockSoundGroup.SAND)));
KELP = register("kelp", new KelpBlock(AbstractBlock.Settings.of(Material.UNDERWATER_PLANT).noCollision().ticksRandomly().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
KELP_PLANT = register("kelp_plant", new KelpPlantBlock(AbstractBlock.Settings.of(Material.UNDERWATER_PLANT).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
DRIED_KELP_BLOCK = register("dried_kelp_block", new Block(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.GREEN).strength(0.5F, 2.5F).sounds(BlockSoundGroup.GRASS)));
TURTLE_EGG = register("turtle_egg", new TurtleEggBlock(AbstractBlock.Settings.of(Material.EGG, MapColor.PALE_YELLOW).strength(0.5F).sounds(BlockSoundGroup.METAL).ticksRandomly().nonOpaque()));
DEAD_TUBE_CORAL_BLOCK = register("dead_tube_coral_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().strength(1.5F, 6.0F)));
DEAD_BRAIN_CORAL_BLOCK = register("dead_brain_coral_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().strength(1.5F, 6.0F)));
DEAD_BUBBLE_CORAL_BLOCK = register("dead_bubble_coral_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().strength(1.5F, 6.0F)));
DEAD_FIRE_CORAL_BLOCK = register("dead_fire_coral_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().strength(1.5F, 6.0F)));
DEAD_HORN_CORAL_BLOCK = register("dead_horn_coral_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().strength(1.5F, 6.0F)));
TUBE_CORAL_BLOCK = register("tube_coral_block", new CoralBlockBlock(DEAD_TUBE_CORAL_BLOCK, AbstractBlock.Settings.of(Material.STONE, MapColor.BLUE).requiresTool().strength(1.5F, 6.0F).sounds(BlockSoundGroup.CORAL)));
BRAIN_CORAL_BLOCK = register("brain_coral_block", new CoralBlockBlock(DEAD_BRAIN_CORAL_BLOCK, AbstractBlock.Settings.of(Material.STONE, MapColor.PINK).requiresTool().strength(1.5F, 6.0F).sounds(BlockSoundGroup.CORAL)));
BUBBLE_CORAL_BLOCK = register("bubble_coral_block", new CoralBlockBlock(DEAD_BUBBLE_CORAL_BLOCK, AbstractBlock.Settings.of(Material.STONE, MapColor.PURPLE).requiresTool().strength(1.5F, 6.0F).sounds(BlockSoundGroup.CORAL)));
FIRE_CORAL_BLOCK = register("fire_coral_block", new CoralBlockBlock(DEAD_FIRE_CORAL_BLOCK, AbstractBlock.Settings.of(Material.STONE, MapColor.RED).requiresTool().strength(1.5F, 6.0F).sounds(BlockSoundGroup.CORAL)));
HORN_CORAL_BLOCK = register("horn_coral_block", new CoralBlockBlock(DEAD_HORN_CORAL_BLOCK, AbstractBlock.Settings.of(Material.STONE, MapColor.YELLOW).requiresTool().strength(1.5F, 6.0F).sounds(BlockSoundGroup.CORAL)));
DEAD_TUBE_CORAL = register("dead_tube_coral", new DeadCoralBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_BRAIN_CORAL = register("dead_brain_coral", new DeadCoralBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_BUBBLE_CORAL = register("dead_bubble_coral", new DeadCoralBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_FIRE_CORAL = register("dead_fire_coral", new DeadCoralBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_HORN_CORAL = register("dead_horn_coral", new DeadCoralBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
TUBE_CORAL = register("tube_coral", new CoralBlock(DEAD_TUBE_CORAL, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.BLUE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
BRAIN_CORAL = register("brain_coral", new CoralBlock(DEAD_BRAIN_CORAL, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PINK).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
BUBBLE_CORAL = register("bubble_coral", new CoralBlock(DEAD_BUBBLE_CORAL, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PURPLE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
FIRE_CORAL = register("fire_coral", new CoralBlock(DEAD_FIRE_CORAL, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.RED).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
HORN_CORAL = register("horn_coral", new CoralBlock(DEAD_HORN_CORAL, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.YELLOW).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
DEAD_TUBE_CORAL_FAN = register("dead_tube_coral_fan", new DeadCoralFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_BRAIN_CORAL_FAN = register("dead_brain_coral_fan", new DeadCoralFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_BUBBLE_CORAL_FAN = register("dead_bubble_coral_fan", new DeadCoralFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_FIRE_CORAL_FAN = register("dead_fire_coral_fan", new DeadCoralFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
DEAD_HORN_CORAL_FAN = register("dead_horn_coral_fan", new DeadCoralFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly()));
TUBE_CORAL_FAN = register("tube_coral_fan", new CoralFanBlock(DEAD_TUBE_CORAL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.BLUE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
BRAIN_CORAL_FAN = register("brain_coral_fan", new CoralFanBlock(DEAD_BRAIN_CORAL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PINK).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
BUBBLE_CORAL_FAN = register("bubble_coral_fan", new CoralFanBlock(DEAD_BUBBLE_CORAL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PURPLE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
FIRE_CORAL_FAN = register("fire_coral_fan", new CoralFanBlock(DEAD_FIRE_CORAL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.RED).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
HORN_CORAL_FAN = register("horn_coral_fan", new CoralFanBlock(DEAD_HORN_CORAL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.YELLOW).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS)));
DEAD_TUBE_CORAL_WALL_FAN = register("dead_tube_coral_wall_fan", new DeadCoralWallFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly().dropsLike(DEAD_TUBE_CORAL_FAN)));
DEAD_BRAIN_CORAL_WALL_FAN = register("dead_brain_coral_wall_fan", new DeadCoralWallFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly().dropsLike(DEAD_BRAIN_CORAL_FAN)));
DEAD_BUBBLE_CORAL_WALL_FAN = register("dead_bubble_coral_wall_fan", new DeadCoralWallFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly().dropsLike(DEAD_BUBBLE_CORAL_FAN)));
DEAD_FIRE_CORAL_WALL_FAN = register("dead_fire_coral_wall_fan", new DeadCoralWallFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly().dropsLike(DEAD_FIRE_CORAL_FAN)));
DEAD_HORN_CORAL_WALL_FAN = register("dead_horn_coral_wall_fan", new DeadCoralWallFanBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.GRAY).requiresTool().noCollision().breakInstantly().dropsLike(DEAD_HORN_CORAL_FAN)));
TUBE_CORAL_WALL_FAN = register("tube_coral_wall_fan", new CoralWallFanBlock(DEAD_TUBE_CORAL_WALL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.BLUE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS).dropsLike(TUBE_CORAL_FAN)));
BRAIN_CORAL_WALL_FAN = register("brain_coral_wall_fan", new CoralWallFanBlock(DEAD_BRAIN_CORAL_WALL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PINK).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS).dropsLike(BRAIN_CORAL_FAN)));
BUBBLE_CORAL_WALL_FAN = register("bubble_coral_wall_fan", new CoralWallFanBlock(DEAD_BUBBLE_CORAL_WALL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.PURPLE).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS).dropsLike(BUBBLE_CORAL_FAN)));
FIRE_CORAL_WALL_FAN = register("fire_coral_wall_fan", new CoralWallFanBlock(DEAD_FIRE_CORAL_WALL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.RED).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS).dropsLike(FIRE_CORAL_FAN)));
HORN_CORAL_WALL_FAN = register("horn_coral_wall_fan", new CoralWallFanBlock(DEAD_HORN_CORAL_WALL_FAN, AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.YELLOW).noCollision().breakInstantly().sounds(BlockSoundGroup.WET_GRASS).dropsLike(HORN_CORAL_FAN)));
SEA_PICKLE = register("sea_pickle", new SeaPickleBlock(AbstractBlock.Settings.of(Material.UNDERWATER_PLANT, MapColor.GREEN).luminance((state) -> {
 return SeaPickleBlock.isDry(state) ? 0 : 3 + 3 * (Integer)state.get(SeaPickleBlock.PICKLES);
}).sounds(BlockSoundGroup.SLIME).nonOpaque()));
BLUE_ICE = register("blue_ice", new TransparentBlock(AbstractBlock.Settings.of(Material.DENSE_ICE).strength(2.8F).slipperiness(0.989F).sounds(BlockSoundGroup.GLASS)));
CONDUIT = register("conduit", new ConduitBlock(AbstractBlock.Settings.of(Material.GLASS, MapColor.DIAMOND_BLUE).strength(3.0F).luminance((state) -> {
 return 15;
}).nonOpaque()));
BAMBOO_SAPLING = register("bamboo_sapling", new BambooSaplingBlock(AbstractBlock.Settings.of(Material.BAMBOO_SAPLING).ticksRandomly().breakInstantly().noCollision().strength(1.0F).sounds(BlockSoundGroup.BAMBOO_SAPLING)));
BAMBOO = register("bamboo", new BambooBlock(AbstractBlock.Settings.of(Material.BAMBOO, MapColor.DARK_GREEN).ticksRandomly().breakInstantly().strength(1.0F).sounds(BlockSoundGroup.BAMBOO).nonOpaque()));
POTTED_BAMBOO = register("potted_bamboo", new FlowerPotBlock(BAMBOO, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
VOID_AIR = register("void_air", new AirBlock(AbstractBlock.Settings.of(Material.AIR).noCollision().dropsNothing().air()));
CAVE_AIR = register("cave_air", new AirBlock(AbstractBlock.Settings.of(Material.AIR).noCollision().dropsNothing().air()));
BUBBLE_COLUMN = register("bubble_column", new BubbleColumnBlock(AbstractBlock.Settings.of(Material.BUBBLE_COLUMN).noCollision().dropsNothing()));
POLISHED_GRANITE_STAIRS = register("polished_granite_stairs", new StairsBlock(POLISHED_GRANITE.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_GRANITE)));
SMOOTH_RED_SANDSTONE_STAIRS = register("smooth_red_sandstone_stairs", new StairsBlock(SMOOTH_RED_SANDSTONE.getDefaultState(), AbstractBlock.Settings.copy(SMOOTH_RED_SANDSTONE)));
MOSSY_STONE_BRICK_STAIRS = register("mossy_stone_brick_stairs", new StairsBlock(MOSSY_STONE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(MOSSY_STONE_BRICKS)));
POLISHED_DIORITE_STAIRS = register("polished_diorite_stairs", new StairsBlock(POLISHED_DIORITE.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_DIORITE)));
MOSSY_COBBLESTONE_STAIRS = register("mossy_cobblestone_stairs", new StairsBlock(MOSSY_COBBLESTONE.getDefaultState(), AbstractBlock.Settings.copy(MOSSY_COBBLESTONE)));
END_STONE_BRICK_STAIRS = register("end_stone_brick_stairs", new StairsBlock(END_STONE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(END_STONE_BRICKS)));
STONE_STAIRS = register("stone_stairs", new StairsBlock(STONE.getDefaultState(), AbstractBlock.Settings.copy(STONE)));
SMOOTH_SANDSTONE_STAIRS = register("smooth_sandstone_stairs", new StairsBlock(SMOOTH_SANDSTONE.getDefaultState(), AbstractBlock.Settings.copy(SMOOTH_SANDSTONE)));
SMOOTH_QUARTZ_STAIRS = register("smooth_quartz_stairs", new StairsBlock(SMOOTH_QUARTZ.getDefaultState(), AbstractBlock.Settings.copy(SMOOTH_QUARTZ)));
GRANITE_STAIRS = register("granite_stairs", new StairsBlock(GRANITE.getDefaultState(), AbstractBlock.Settings.copy(GRANITE)));
ANDESITE_STAIRS = register("andesite_stairs", new StairsBlock(ANDESITE.getDefaultState(), AbstractBlock.Settings.copy(ANDESITE)));
RED_NETHER_BRICK_STAIRS = register("red_nether_brick_stairs", new StairsBlock(RED_NETHER_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(RED_NETHER_BRICKS)));
POLISHED_ANDESITE_STAIRS = register("polished_andesite_stairs", new StairsBlock(POLISHED_ANDESITE.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_ANDESITE)));
DIORITE_STAIRS = register("diorite_stairs", new StairsBlock(DIORITE.getDefaultState(), AbstractBlock.Settings.copy(DIORITE)));
POLISHED_GRANITE_SLAB = register("polished_granite_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_GRANITE)));
SMOOTH_RED_SANDSTONE_SLAB = register("smooth_red_sandstone_slab", new SlabBlock(AbstractBlock.Settings.copy(SMOOTH_RED_SANDSTONE)));
MOSSY_STONE_BRICK_SLAB = register("mossy_stone_brick_slab", new SlabBlock(AbstractBlock.Settings.copy(MOSSY_STONE_BRICKS)));
POLISHED_DIORITE_SLAB = register("polished_diorite_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_DIORITE)));
MOSSY_COBBLESTONE_SLAB = register("mossy_cobblestone_slab", new SlabBlock(AbstractBlock.Settings.copy(MOSSY_COBBLESTONE)));
END_STONE_BRICK_SLAB = register("end_stone_brick_slab", new SlabBlock(AbstractBlock.Settings.copy(END_STONE_BRICKS)));
SMOOTH_SANDSTONE_SLAB = register("smooth_sandstone_slab", new SlabBlock(AbstractBlock.Settings.copy(SMOOTH_SANDSTONE)));
SMOOTH_QUARTZ_SLAB = register("smooth_quartz_slab", new SlabBlock(AbstractBlock.Settings.copy(SMOOTH_QUARTZ)));
GRANITE_SLAB = register("granite_slab", new SlabBlock(AbstractBlock.Settings.copy(GRANITE)));
ANDESITE_SLAB = register("andesite_slab", new SlabBlock(AbstractBlock.Settings.copy(ANDESITE)));
RED_NETHER_BRICK_SLAB = register("red_nether_brick_slab", new SlabBlock(AbstractBlock.Settings.copy(RED_NETHER_BRICKS)));
POLISHED_ANDESITE_SLAB = register("polished_andesite_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_ANDESITE)));
DIORITE_SLAB = register("diorite_slab", new SlabBlock(AbstractBlock.Settings.copy(DIORITE)));
BRICK_WALL = register("brick_wall", new WallBlock(AbstractBlock.Settings.copy(BRICKS)));
PRISMARINE_WALL = register("prismarine_wall", new WallBlock(AbstractBlock.Settings.copy(PRISMARINE)));
RED_SANDSTONE_WALL = register("red_sandstone_wall", new WallBlock(AbstractBlock.Settings.copy(RED_SANDSTONE)));
MOSSY_STONE_BRICK_WALL = register("mossy_stone_brick_wall", new WallBlock(AbstractBlock.Settings.copy(MOSSY_STONE_BRICKS)));
GRANITE_WALL = register("granite_wall", new WallBlock(AbstractBlock.Settings.copy(GRANITE)));
STONE_BRICK_WALL = register("stone_brick_wall", new WallBlock(AbstractBlock.Settings.copy(STONE_BRICKS)));
NETHER_BRICK_WALL = register("nether_brick_wall", new WallBlock(AbstractBlock.Settings.copy(NETHER_BRICKS)));
ANDESITE_WALL = register("andesite_wall", new WallBlock(AbstractBlock.Settings.copy(ANDESITE)));
RED_NETHER_BRICK_WALL = register("red_nether_brick_wall", new WallBlock(AbstractBlock.Settings.copy(RED_NETHER_BRICKS)));
SANDSTONE_WALL = register("sandstone_wall", new WallBlock(AbstractBlock.Settings.copy(SANDSTONE)));
END_STONE_BRICK_WALL = register("end_stone_brick_wall", new WallBlock(AbstractBlock.Settings.copy(END_STONE_BRICKS)));
DIORITE_WALL = register("diorite_wall", new WallBlock(AbstractBlock.Settings.copy(DIORITE)));
SCAFFOLDING = register("scaffolding", new ScaffoldingBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.PALE_YELLOW).noCollision().sounds(BlockSoundGroup.SCAFFOLDING).dynamicBounds()));
LOOM = register("loom", new LoomBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
BARREL = register("barrel", new BarrelBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
SMOKER = register("smoker", new SmokerBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(3.5F).luminance(createLightLevelFromLitBlockState(13))));
BLAST_FURNACE = register("blast_furnace", new BlastFurnaceBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(3.5F).luminance(createLightLevelFromLitBlockState(13))));
CARTOGRAPHY_TABLE = register("cartography_table", new CartographyTableBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
FLETCHING_TABLE = register("fletching_table", new FletchingTableBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
GRINDSTONE = register("grindstone", new GrindstoneBlock(AbstractBlock.Settings.of(Material.REPAIR_STATION, MapColor.IRON_GRAY).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.STONE)));
LECTERN = register("lectern", new LecternBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
SMITHING_TABLE = register("smithing_table", new SmithingTableBlock(AbstractBlock.Settings.of(Material.WOOD).strength(2.5F).sounds(BlockSoundGroup.WOOD)));
STONECUTTER = register("stonecutter", new StonecutterBlock(AbstractBlock.Settings.of(Material.STONE).requiresTool().strength(3.5F)));
BELL = register("bell", new BellBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.GOLD).requiresTool().strength(5.0F).sounds(BlockSoundGroup.ANVIL)));
LANTERN = register("lantern", new LanternBlock(AbstractBlock.Settings.of(Material.METAL).requiresTool().strength(3.5F).sounds(BlockSoundGroup.LANTERN).luminance((state) -> {
 return 15;
}).nonOpaque()));
SOUL_LANTERN = register("soul_lantern", new LanternBlock(AbstractBlock.Settings.of(Material.METAL).requiresTool().strength(3.5F).sounds(BlockSoundGroup.LANTERN).luminance((state) -> {
 return 10;
}).nonOpaque()));
CAMPFIRE = register("campfire", new CampfireBlock(true, 1, AbstractBlock.Settings.of(Material.WOOD, MapColor.SPRUCE_BROWN).strength(2.0F).sounds(BlockSoundGroup.WOOD).luminance(createLightLevelFromLitBlockState(15)).nonOpaque()));
SOUL_CAMPFIRE = register("soul_campfire", new CampfireBlock(false, 2, AbstractBlock.Settings.of(Material.WOOD, MapColor.SPRUCE_BROWN).strength(2.0F).sounds(BlockSoundGroup.WOOD).luminance(createLightLevelFromLitBlockState(10)).nonOpaque()));
SWEET_BERRY_BUSH = register("sweet_berry_bush", new SweetBerryBushBlock(AbstractBlock.Settings.of(Material.PLANT).ticksRandomly().noCollision().sounds(BlockSoundGroup.SWEET_BERRY_BUSH)));
WARPED_STEM = register("warped_stem", createNetherStemBlock(MapColor.DARK_AQUA));
STRIPPED_WARPED_STEM = register("stripped_warped_stem", createNetherStemBlock(MapColor.DARK_AQUA));
WARPED_HYPHAE = register("warped_hyphae", new PillarBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DARK_DULL_PINK).strength(2.0F).sounds(BlockSoundGroup.NETHER_STEM)));
STRIPPED_WARPED_HYPHAE = register("stripped_warped_hyphae", new PillarBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DARK_DULL_PINK).strength(2.0F).sounds(BlockSoundGroup.NETHER_STEM)));
WARPED_NYLIUM = register("warped_nylium", new NyliumBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.TEAL).requiresTool().strength(0.4F).sounds(BlockSoundGroup.NYLIUM).ticksRandomly()));
WARPED_FUNGUS = register("warped_fungus", new FungusBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.CYAN).breakInstantly().noCollision().sounds(BlockSoundGroup.FUNGUS), () -> {
 return ConfiguredFeatures.WARPED_FUNGI_PLANTED;
}));
WARPED_WART_BLOCK = register("warped_wart_block", new Block(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.BRIGHT_TEAL).strength(1.0F).sounds(BlockSoundGroup.WART_BLOCK)));
WARPED_ROOTS = register("warped_roots", new RootsBlock(AbstractBlock.Settings.of(Material.NETHER_SHOOTS, MapColor.CYAN).noCollision().breakInstantly().sounds(BlockSoundGroup.ROOTS)));
NETHER_SPROUTS = register("nether_sprouts", new SproutsBlock(AbstractBlock.Settings.of(Material.NETHER_SHOOTS, MapColor.CYAN).noCollision().breakInstantly().sounds(BlockSoundGroup.NETHER_SPROUTS)));
CRIMSON_STEM = register("crimson_stem", createNetherStemBlock(MapColor.DULL_PINK));
STRIPPED_CRIMSON_STEM = register("stripped_crimson_stem", createNetherStemBlock(MapColor.DULL_PINK));
CRIMSON_HYPHAE = register("crimson_hyphae", new PillarBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DARK_CRIMSON).strength(2.0F).sounds(BlockSoundGroup.NETHER_STEM)));
STRIPPED_CRIMSON_HYPHAE = register("stripped_crimson_hyphae", new PillarBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DARK_CRIMSON).strength(2.0F).sounds(BlockSoundGroup.NETHER_STEM)));
CRIMSON_NYLIUM = register("crimson_nylium", new NyliumBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.DULL_RED).requiresTool().strength(0.4F).sounds(BlockSoundGroup.NYLIUM).ticksRandomly()));
CRIMSON_FUNGUS = register("crimson_fungus", new FungusBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.DARK_RED).breakInstantly().noCollision().sounds(BlockSoundGroup.FUNGUS), () -> {
 return ConfiguredFeatures.CRIMSON_FUNGI_PLANTED;
}));
SHROOMLIGHT = register("shroomlight", new Block(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.RED).strength(1.0F).sounds(BlockSoundGroup.SHROOMLIGHT).luminance((state) -> {
 return 15;
})));
WEEPING_VINES = register("weeping_vines", new WeepingVinesBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.DARK_RED).ticksRandomly().noCollision().breakInstantly().sounds(BlockSoundGroup.WEEPING_VINES)));
WEEPING_VINES_PLANT = register("weeping_vines_plant", new WeepingVinesPlantBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.DARK_RED).noCollision().breakInstantly().sounds(BlockSoundGroup.WEEPING_VINES)));
TWISTING_VINES = register("twisting_vines", new TwistingVinesBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.CYAN).ticksRandomly().noCollision().breakInstantly().sounds(BlockSoundGroup.WEEPING_VINES)));
TWISTING_VINES_PLANT = register("twisting_vines_plant", new TwistingVinesPlantBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.CYAN).noCollision().breakInstantly().sounds(BlockSoundGroup.WEEPING_VINES)));
CRIMSON_ROOTS = register("crimson_roots", new RootsBlock(AbstractBlock.Settings.of(Material.NETHER_SHOOTS, MapColor.DARK_RED).noCollision().breakInstantly().sounds(BlockSoundGroup.ROOTS)));
CRIMSON_PLANKS = register("crimson_planks", new Block(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DULL_PINK).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
WARPED_PLANKS = register("warped_planks", new Block(AbstractBlock.Settings.of(Material.NETHER_WOOD, MapColor.DARK_AQUA).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_SLAB = register("crimson_slab", new SlabBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
WARPED_SLAB = register("warped_slab", new SlabBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_PRESSURE_PLATE = register("crimson_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
WARPED_PRESSURE_PLATE = register("warped_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.EVERYTHING, AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_FENCE = register("crimson_fence", new FenceBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
WARPED_FENCE = register("warped_fence", new FenceBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_TRAPDOOR = register("crimson_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
WARPED_TRAPDOOR = register("warped_trapdoor", new TrapdoorBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque().allowsSpawning(Blocks::never)));
CRIMSON_FENCE_GATE = register("crimson_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
WARPED_FENCE_GATE = register("warped_fence_gate", new FenceGateBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).strength(2.0F, 3.0F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_STAIRS = register("crimson_stairs", new StairsBlock(CRIMSON_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(CRIMSON_PLANKS)));
WARPED_STAIRS = register("warped_stairs", new StairsBlock(WARPED_PLANKS.getDefaultState(), AbstractBlock.Settings.copy(WARPED_PLANKS)));
CRIMSON_BUTTON = register("crimson_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
WARPED_BUTTON = register("warped_button", new WoodenButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F).sounds(BlockSoundGroup.WOOD)));
CRIMSON_DOOR = register("crimson_door", new DoorBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
WARPED_DOOR = register("warped_door", new DoorBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).strength(3.0F).sounds(BlockSoundGroup.WOOD).nonOpaque()));
CRIMSON_SIGN = register("crimson_sign", new SignBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.CRIMSON));
WARPED_SIGN = register("warped_sign", new SignBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD), SignType.WARPED));
CRIMSON_WALL_SIGN = register("crimson_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, CRIMSON_PLANKS.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(CRIMSON_SIGN), SignType.CRIMSON));
WARPED_WALL_SIGN = register("warped_wall_sign", new WallSignBlock(AbstractBlock.Settings.of(Material.NETHER_WOOD, WARPED_PLANKS.getDefaultMapColor()).noCollision().strength(1.0F).sounds(BlockSoundGroup.WOOD).dropsLike(WARPED_SIGN), SignType.WARPED));
STRUCTURE_BLOCK = register("structure_block", new StructureBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.LIGHT_GRAY).requiresTool().strength(-1.0F, 3600000.0F).dropsNothing()));
JIGSAW = register("jigsaw", new JigsawBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.LIGHT_GRAY).requiresTool().strength(-1.0F, 3600000.0F).dropsNothing()));
COMPOSTER = register("composter", new ComposterBlock(AbstractBlock.Settings.of(Material.WOOD).strength(0.6F).sounds(BlockSoundGroup.WOOD)));
TARGET = register("target", new TargetBlock(AbstractBlock.Settings.of(Material.SOLID_ORGANIC, MapColor.OFF_WHITE).strength(0.5F).sounds(BlockSoundGroup.GRASS)));
BEE_NEST = register("bee_nest", new BeehiveBlock(AbstractBlock.Settings.of(Material.WOOD, MapColor.YELLOW).strength(0.3F).sounds(BlockSoundGroup.WOOD)));
BEEHIVE = register("beehive", new BeehiveBlock(AbstractBlock.Settings.of(Material.WOOD).strength(0.6F).sounds(BlockSoundGroup.WOOD)));
HONEY_BLOCK = register("honey_block", new HoneyBlock(AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT, MapColor.ORANGE).velocityMultiplier(0.4F).jumpVelocityMultiplier(0.5F).nonOpaque().sounds(BlockSoundGroup.HONEY)));
HONEYCOMB_BLOCK = register("honeycomb_block", new Block(AbstractBlock.Settings.of(Material.ORGANIC_PRODUCT, MapColor.ORANGE).strength(0.6F).sounds(BlockSoundGroup.CORAL)));
NETHERITE_BLOCK = register("netherite_block", new Block(AbstractBlock.Settings.of(Material.METAL, MapColor.BLACK).requiresTool().strength(50.0F, 1200.0F).sounds(BlockSoundGroup.NETHERITE)));
ANCIENT_DEBRIS = register("ancient_debris", new Block(AbstractBlock.Settings.of(Material.METAL, MapColor.BLACK).requiresTool().strength(30.0F, 1200.0F).sounds(BlockSoundGroup.ANCIENT_DEBRIS)));
CRYING_OBSIDIAN = register("crying_obsidian", new CryingObsidianBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(50.0F, 1200.0F).luminance((state) -> {
 return 10;
})));
RESPAWN_ANCHOR = register("respawn_anchor", new RespawnAnchorBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(50.0F, 1200.0F).luminance((state) -> {
 return RespawnAnchorBlock.getLightLevel(state, 15);
})));
POTTED_CRIMSON_FUNGUS = register("potted_crimson_fungus", new FlowerPotBlock(CRIMSON_FUNGUS, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_WARPED_FUNGUS = register("potted_warped_fungus", new FlowerPotBlock(WARPED_FUNGUS, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_CRIMSON_ROOTS = register("potted_crimson_roots", new FlowerPotBlock(CRIMSON_ROOTS, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
POTTED_WARPED_ROOTS = register("potted_warped_roots", new FlowerPotBlock(WARPED_ROOTS, AbstractBlock.Settings.of(Material.DECORATION).breakInstantly().nonOpaque()));
LODESTONE = register("lodestone", new Block(AbstractBlock.Settings.of(Material.REPAIR_STATION).requiresTool().strength(3.5F).sounds(BlockSoundGroup.LODESTONE)));
BLACKSTONE = register("blackstone", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().strength(1.5F, 6.0F)));
BLACKSTONE_STAIRS = register("blackstone_stairs", new StairsBlock(BLACKSTONE.getDefaultState(), AbstractBlock.Settings.copy(BLACKSTONE)));
BLACKSTONE_WALL = register("blackstone_wall", new WallBlock(AbstractBlock.Settings.copy(BLACKSTONE)));
BLACKSTONE_SLAB = register("blackstone_slab", new SlabBlock(AbstractBlock.Settings.copy(BLACKSTONE).strength(2.0F, 6.0F)));
POLISHED_BLACKSTONE = register("polished_blackstone", new Block(AbstractBlock.Settings.copy(BLACKSTONE).strength(2.0F, 6.0F)));
POLISHED_BLACKSTONE_BRICKS = register("polished_blackstone_bricks", new Block(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE).strength(1.5F, 6.0F)));
CRACKED_POLISHED_BLACKSTONE_BRICKS = register("cracked_polished_blackstone_bricks", new Block(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE_BRICKS)));
CHISELED_POLISHED_BLACKSTONE = register("chiseled_polished_blackstone", new Block(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE).strength(1.5F, 6.0F)));
POLISHED_BLACKSTONE_BRICK_SLAB = register("polished_blackstone_brick_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE_BRICKS).strength(2.0F, 6.0F)));
POLISHED_BLACKSTONE_BRICK_STAIRS = register("polished_blackstone_brick_stairs", new StairsBlock(POLISHED_BLACKSTONE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_BLACKSTONE_BRICKS)));
POLISHED_BLACKSTONE_BRICK_WALL = register("polished_blackstone_brick_wall", new WallBlock(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE_BRICKS)));
GILDED_BLACKSTONE = register("gilded_blackstone", new Block(AbstractBlock.Settings.copy(BLACKSTONE).sounds(BlockSoundGroup.GILDED_BLACKSTONE)));
POLISHED_BLACKSTONE_STAIRS = register("polished_blackstone_stairs", new StairsBlock(POLISHED_BLACKSTONE.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_BLACKSTONE)));
POLISHED_BLACKSTONE_SLAB = register("polished_blackstone_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE)));
POLISHED_BLACKSTONE_PRESSURE_PLATE = register("polished_blackstone_pressure_plate", new PressurePlateBlock(PressurePlateBlock.ActivationRule.MOBS, AbstractBlock.Settings.of(Material.STONE, MapColor.BLACK).requiresTool().noCollision().strength(0.5F)));
POLISHED_BLACKSTONE_BUTTON = register("polished_blackstone_button", new StoneButtonBlock(AbstractBlock.Settings.of(Material.DECORATION).noCollision().strength(0.5F)));
POLISHED_BLACKSTONE_WALL = register("polished_blackstone_wall", new WallBlock(AbstractBlock.Settings.copy(POLISHED_BLACKSTONE)));
CHISELED_NETHER_BRICKS = register("chiseled_nether_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
CRACKED_NETHER_BRICKS = register("cracked_nether_bricks", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.DARK_RED).requiresTool().strength(2.0F, 6.0F).sounds(BlockSoundGroup.NETHER_BRICKS)));
QUARTZ_BRICKS = register("quartz_bricks", new Block(AbstractBlock.Settings.copy(QUARTZ_BLOCK)));
CANDLE = register("candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.PALE_YELLOW).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
WHITE_CANDLE = register("white_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.WHITE_GRAY).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
ORANGE_CANDLE = register("orange_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.ORANGE).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
MAGENTA_CANDLE = register("magenta_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.MAGENTA).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
LIGHT_BLUE_CANDLE = register("light_blue_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.LIGHT_BLUE).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
YELLOW_CANDLE = register("yellow_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.YELLOW).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
LIME_CANDLE = register("lime_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.LIME).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
PINK_CANDLE = register("pink_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.PINK).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
GRAY_CANDLE = register("gray_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.GRAY).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
LIGHT_GRAY_CANDLE = register("light_gray_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.LIGHT_GRAY).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
CYAN_CANDLE = register("cyan_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.CYAN).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
PURPLE_CANDLE = register("purple_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.PURPLE).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
BLUE_CANDLE = register("blue_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.BLUE).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
BROWN_CANDLE = register("brown_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.BROWN).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
GREEN_CANDLE = register("green_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.GREEN).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
RED_CANDLE = register("red_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.RED).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
BLACK_CANDLE = register("black_candle", new CandleBlock(AbstractBlock.Settings.of(Material.DECORATION, MapColor.BLACK).nonOpaque().strength(0.1F).sounds(BlockSoundGroup.CANDLE).luminance(CandleBlock.STATE_TO_LUMINANCE)));
CANDLE_CAKE = register("candle_cake", new CandleCakeBlock(CANDLE, AbstractBlock.Settings.copy(CAKE).luminance(createLightLevelFromLitBlockState(3))));
WHITE_CANDLE_CAKE = register("white_candle_cake", new CandleCakeBlock(WHITE_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
ORANGE_CANDLE_CAKE = register("orange_candle_cake", new CandleCakeBlock(ORANGE_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
MAGENTA_CANDLE_CAKE = register("magenta_candle_cake", new CandleCakeBlock(MAGENTA_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
LIGHT_BLUE_CANDLE_CAKE = register("light_blue_candle_cake", new CandleCakeBlock(LIGHT_BLUE_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
YELLOW_CANDLE_CAKE = register("yellow_candle_cake", new CandleCakeBlock(YELLOW_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
LIME_CANDLE_CAKE = register("lime_candle_cake", new CandleCakeBlock(LIME_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
PINK_CANDLE_CAKE = register("pink_candle_cake", new CandleCakeBlock(PINK_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
GRAY_CANDLE_CAKE = register("gray_candle_cake", new CandleCakeBlock(GRAY_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
LIGHT_GRAY_CANDLE_CAKE = register("light_gray_candle_cake", new CandleCakeBlock(LIGHT_GRAY_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
CYAN_CANDLE_CAKE = register("cyan_candle_cake", new CandleCakeBlock(CYAN_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
PURPLE_CANDLE_CAKE = register("purple_candle_cake", new CandleCakeBlock(PURPLE_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
BLUE_CANDLE_CAKE = register("blue_candle_cake", new CandleCakeBlock(BLUE_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
BROWN_CANDLE_CAKE = register("brown_candle_cake", new CandleCakeBlock(BROWN_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
GREEN_CANDLE_CAKE = register("green_candle_cake", new CandleCakeBlock(GREEN_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
RED_CANDLE_CAKE = register("red_candle_cake", new CandleCakeBlock(RED_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
BLACK_CANDLE_CAKE = register("black_candle_cake", new CandleCakeBlock(BLACK_CANDLE, AbstractBlock.Settings.copy(CANDLE_CAKE)));
AMETHYST_BLOCK = register("amethyst_block", new AmethystBlock(AbstractBlock.Settings.of(Material.AMETHYST, MapColor.PURPLE).strength(1.5F).sounds(BlockSoundGroup.AMETHYST_BLOCK).requiresTool()));
BUDDING_AMETHYST = register("budding_amethyst", new BuddingAmethystBlock(AbstractBlock.Settings.of(Material.AMETHYST).ticksRandomly().strength(1.5F).sounds(BlockSoundGroup.AMETHYST_BLOCK).requiresTool()));
AMETHYST_CLUSTER = register("amethyst_cluster", new AmethystClusterBlock(7, 3, AbstractBlock.Settings.of(Material.AMETHYST).nonOpaque().requiresTool().ticksRandomly().sounds(BlockSoundGroup.AMETHYST_CLUSTER).strength(1.5F).luminance(createLightLevelFromLitBlockState(5))));
LARGE_AMETHYST_BUD = register("large_amethyst_bud", new AmethystClusterBlock(5, 3, AbstractBlock.Settings.copy(AMETHYST_CLUSTER).sounds(BlockSoundGroup.MEDIUM_AMETHYST_BUD).luminance(createLightLevelFromLitBlockState(4))));
MEDIUM_AMETHYST_BUD = register("medium_amethyst_bud", new AmethystClusterBlock(4, 3, AbstractBlock.Settings.copy(AMETHYST_CLUSTER).sounds(BlockSoundGroup.LARGE_AMETHYST_BUD).luminance(createLightLevelFromLitBlockState(2))));
SMALL_AMETHYST_BUD = register("small_amethyst_bud", new AmethystClusterBlock(3, 4, AbstractBlock.Settings.copy(AMETHYST_CLUSTER).sounds(BlockSoundGroup.SMALL_AMETHYST_BUD).luminance(createLightLevelFromLitBlockState(1))));
TUFF = register("tuff", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_GRAY).sounds(BlockSoundGroup.TUFF).requiresTool().strength(1.5F, 6.0F)));
CALCITE = register("calcite", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_WHITE).sounds(BlockSoundGroup.CALCITE).requiresTool().strength(0.75F)));
TINTED_GLASS = register("tinted_glass", new TintedGlassBlock(AbstractBlock.Settings.copy(GLASS).mapColor(MapColor.GRAY)));
POWDER_SNOW = register("powder_snow", new PowderSnowBlock(AbstractBlock.Settings.of(Material.POWDER_SNOW).strength(0.1F).sounds(BlockSoundGroup.POWDER_SNOW).dynamicBounds()));
SCULK_SENSOR = register("sculk_sensor", new SculkSensorBlock(AbstractBlock.Settings.of(Material.SCULK, MapColor.CYAN).strength(1.5F).sounds(BlockSoundGroup.SCULK_SENSOR).luminance((state) -> {
 return 1;
}).emissiveLighting((state, world, pos) -> {
 return SculkSensorBlock.getPhase(state) == SculkSensorPhase.ACTIVE;
}), 8));
OXIDIZED_COPPER = register("oxidized_copper", new OxidizableBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.TEAL).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.COPPER)));
WEATHERED_COPPER = register("weathered_copper", new OxidizableBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.DARK_AQUA).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.COPPER), Oxidizable.OxidizationLevel.WEATHERED, OXIDIZED_COPPER));
EXPOSED_COPPER = register("exposed_copper", new OxidizableBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.TERRACOTTA_LIGHT_GRAY).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.COPPER), Oxidizable.OxidizationLevel.EXPOSED, WEATHERED_COPPER));
COPPER_BLOCK = register("copper_block", new OxidizableBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.ORANGE).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.COPPER), Oxidizable.OxidizationLevel.UNAFFECTED, EXPOSED_COPPER));
COPPER_ORE = register("copper_ore", new Block(AbstractBlock.Settings.copy(IRON_ORE)));
OXIDIZED_CUT_COPPER = register("oxidized_cut_copper", new OxidizableBlock(AbstractBlock.Settings.copy(OXIDIZED_COPPER)));
WEATHERED_CUT_COPPER = register("weathered_cut_copper", new OxidizableBlock(AbstractBlock.Settings.copy(WEATHERED_COPPER), Oxidizable.OxidizationLevel.WEATHERED, OXIDIZED_CUT_COPPER));
EXPOSED_CUT_COPPER = register("exposed_cut_copper", new OxidizableBlock(AbstractBlock.Settings.copy(EXPOSED_COPPER), Oxidizable.OxidizationLevel.EXPOSED, WEATHERED_CUT_COPPER));
CUT_COPPER = register("cut_copper", new OxidizableBlock(AbstractBlock.Settings.copy(COPPER_BLOCK), Oxidizable.OxidizationLevel.UNAFFECTED, EXPOSED_CUT_COPPER));
OXIDIZED_CUT_COPPER_STAIRS = register("oxidized_cut_copper_stairs", new OxidizableStairsBlock(OXIDIZED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(OXIDIZED_CUT_COPPER)));
WEATHERED_CUT_COPPER_STAIRS = register("weathered_cut_copper_stairs", new OxidizableStairsBlock(WEATHERED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(WEATHERED_COPPER), Oxidizable.OxidizationLevel.WEATHERED, OXIDIZED_CUT_COPPER_STAIRS));
EXPOSED_CUT_COPPER_STAIRS = register("exposed_cut_copper_stairs", new OxidizableStairsBlock(EXPOSED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(EXPOSED_COPPER), Oxidizable.OxidizationLevel.EXPOSED, WEATHERED_CUT_COPPER_STAIRS));
CUT_COPPER_STAIRS = register("cut_copper_stairs", new OxidizableStairsBlock(CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(COPPER_BLOCK), Oxidizable.OxidizationLevel.UNAFFECTED, EXPOSED_CUT_COPPER_STAIRS));
OXIDIZED_CUT_COPPER_SLAB = register("oxidized_cut_copper_slab", new OxidizableSlabBlock(AbstractBlock.Settings.copy(OXIDIZED_CUT_COPPER).requiresTool()));
WEATHERED_CUT_COPPER_SLAB = register("weathered_cut_copper_slab", new OxidizableSlabBlock(AbstractBlock.Settings.copy(WEATHERED_CUT_COPPER).requiresTool(), Oxidizable.OxidizationLevel.WEATHERED, OXIDIZED_CUT_COPPER_SLAB));
EXPOSED_CUT_COPPER_SLAB = register("exposed_cut_copper_slab", new OxidizableSlabBlock(AbstractBlock.Settings.copy(EXPOSED_CUT_COPPER).requiresTool(), Oxidizable.OxidizationLevel.EXPOSED, WEATHERED_CUT_COPPER_SLAB));
CUT_COPPER_SLAB = register("cut_copper_slab", new OxidizableSlabBlock(AbstractBlock.Settings.copy(CUT_COPPER).requiresTool(), Oxidizable.OxidizationLevel.UNAFFECTED, EXPOSED_CUT_COPPER_SLAB));
WAXED_COPPER_BLOCK = register("waxed_copper_block", new Block(AbstractBlock.Settings.copy(COPPER_BLOCK)));
WAXED_WEATHERED_COPPER = register("waxed_weathered_copper", new Block(AbstractBlock.Settings.copy(WEATHERED_COPPER)));
WAXED_EXPOSED_COPPER = register("waxed_exposed_copper", new Block(AbstractBlock.Settings.copy(EXPOSED_COPPER)));
WAXED_WEATHERED_CUT_COPPER = register("waxed_weathered_cut_copper", new Block(AbstractBlock.Settings.copy(WEATHERED_COPPER)));
WAXED_EXPOSED_CUT_COPPER = register("waxed_exposed_cut_copper", new Block(AbstractBlock.Settings.copy(EXPOSED_COPPER)));
WAXED_CUT_COPPER = register("waxed_cut_copper", new Block(AbstractBlock.Settings.copy(COPPER_BLOCK)));
WAXED_WEATHERED_CUT_COPPER_STAIRS = register("waxed_weathered_cut_copper_stairs", new StairsBlock(WAXED_WEATHERED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(WEATHERED_COPPER)));
WAXED_EXPOSED_CUT_COPPER_STAIRS = register("waxed_exposed_cut_copper_stairs", new StairsBlock(WAXED_EXPOSED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(EXPOSED_COPPER)));
WAXED_CUT_COPPER_STAIRS = register("waxed_cut_copper_stairs", new StairsBlock(WAXED_CUT_COPPER.getDefaultState(), AbstractBlock.Settings.copy(COPPER_BLOCK)));
WAXED_WEATHERED_CUT_COPPER_SLAB = register("waxed_weathered_cut_copper_slab", new SlabBlock(AbstractBlock.Settings.copy(WAXED_WEATHERED_CUT_COPPER).requiresTool()));
WAXED_EXPOSED_CUT_COPPER_SLAB = register("waxed_exposed_cut_copper_slab", new SlabBlock(AbstractBlock.Settings.copy(WAXED_EXPOSED_CUT_COPPER).requiresTool()));
WAXED_CUT_COPPER_SLAB = register("waxed_cut_copper_slab", new SlabBlock(AbstractBlock.Settings.copy(WAXED_CUT_COPPER).requiresTool()));
LIGHTNING_ROD = register("lightning_rod", new LightningRodBlock(AbstractBlock.Settings.of(Material.METAL, MapColor.ORANGE).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.COPPER).nonOpaque()));
POINTED_DRIPSTONE = register("pointed_dripstone", new PointedDripstoneBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_BROWN).nonOpaque().sounds(BlockSoundGroup.POINTED_DRIPSTONE).ticksRandomly().strength(1.5F, 3.0F)));
DRIPSTONE_BLOCK = register("dripstone_block", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.TERRACOTTA_BROWN).sounds(BlockSoundGroup.DRIPSTONE_BLOCK).requiresTool().strength(1.5F, 1.0F)));
CAVE_VINES_HEAD = register("cave_vines_head", new CaveVinesHeadBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).ticksRandomly().noCollision().luminance(createLightLevelFromBerriesBlockState(10)).breakInstantly().sounds(BlockSoundGroup.CAVE_VINES)));
CAVE_VINES_BODY = register("cave_vines_body", new CaveVinesBodyBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).noCollision().luminance(createLightLevelFromBerriesBlockState(14)).breakInstantly().sounds(BlockSoundGroup.CAVE_VINES)));
SPORE_BLOSSOM = register("spore_blossom", new SporeBlossomBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).noCollision().sounds(BlockSoundGroup.SPORE_BLOSSOM)));
AZALEA = register("azalea", new AzaleaBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).sounds(BlockSoundGroup.AZALEA).nonOpaque()));
FLOWERING_AZALEA = register("flowering_azalea", new AzaleaBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).sounds(BlockSoundGroup.FLOWERING_AZALEA).nonOpaque()));
MOSS_CARPET = register("moss_carpet", new CarpetBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).strength(0.1F).sounds(BlockSoundGroup.MOSS_CARPET)));
MOSS_BLOCK = register("moss_block", new MossBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).strength(0.1F).sounds(BlockSoundGroup.MOSS)));
BIG_DRIPLEAF = register("big_dripleaf", new BigDripleafBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).strength(0.1F).sounds(BlockSoundGroup.BIG_DRIPLEAF)));
BIG_DRIPLEAF_STEM = register("big_dripleaf_stem", new BigDripleafStemBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).noCollision().strength(0.1F).sounds(BlockSoundGroup.BIG_DRIPLEAF)));
SMALL_DRIPLEAF = register("small_dripleaf", new SmallDripleafBlock(AbstractBlock.Settings.of(Material.PLANT, MapColor.GREEN).strength(0.1F).noCollision().breakInstantly().sounds(BlockSoundGroup.SMALL_DRIPLEAF)));
ROOTED_DIRT = register("rooted_dirt", new Block(AbstractBlock.Settings.of(Material.SOIL, MapColor.DIRT_BROWN).strength(0.1F).sounds(BlockSoundGroup.ROOTED_DIRT)));
HANGING_ROOTS = register("hanging_roots", new HangingRootsBlock(AbstractBlock.Settings.of(Material.SOIL, MapColor.DIRT_BROWN).noCollision().breakInstantly().strength(0.1F).sounds(BlockSoundGroup.HANGING_ROOTS)));
DEEPSLATE = register("deepslate", new Block(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(3.0F, 6.0F).sounds(BlockSoundGroup.DEEPSLATE)));
COBBLED_DEEPSLATE = register("cobbled_deepslate", new Block(AbstractBlock.Settings.copy(DEEPSLATE)));
COBBLED_DEEPSLATE_STAIRS = register("cobbled_deepslate_stairs", new StairsBlock(COBBLED_DEEPSLATE.getDefaultState(), AbstractBlock.Settings.copy(COBBLED_DEEPSLATE)));
COBBLED_DEEPSLATE_SLAB = register("cobbled_deepslate_slab", new SlabBlock(AbstractBlock.Settings.of(Material.STONE, MapColor.STONE_GRAY).requiresTool().strength(3.5F, 6.0F)));
COBBLED_DEEPSLATE_WALL = register("cobbled_deepslate_wall", new WallBlock(AbstractBlock.Settings.copy(COBBLED_DEEPSLATE)));
POLISHED_DEEPSLATE = register("polished_deepslate", new Block(AbstractBlock.Settings.copy(COBBLED_DEEPSLATE).strength(3.5F, 6.0F).sounds(BlockSoundGroup.POLISHED_DEEPSLATE)));
POLISHED_DEEPSLATE_STAIRS = register("polished_deepslate_stairs", new StairsBlock(POLISHED_DEEPSLATE.getDefaultState(), AbstractBlock.Settings.copy(POLISHED_DEEPSLATE)));
POLISHED_DEEPSLATE_SLAB = register("polished_deepslate_slab", new SlabBlock(AbstractBlock.Settings.copy(POLISHED_DEEPSLATE)));
POLISHED_DEEPSLATE_WALL = register("polished_deepslate_wall", new WallBlock(AbstractBlock.Settings.copy(POLISHED_DEEPSLATE)));
DEEPSLATE_TILES = register("deepslate_tiles", new Block(AbstractBlock.Settings.copy(COBBLED_DEEPSLATE).strength(1.5F, 6.0F).sounds(BlockSoundGroup.DEEPSLATE_TILES)));
DEEPSLATE_TILE_STAIRS = register("deepslate_tile_stairs", new StairsBlock(DEEPSLATE_TILES.getDefaultState(), AbstractBlock.Settings.copy(DEEPSLATE_TILES)));
DEEPSLATE_TILE_SLAB = register("deepslate_tile_slab", new SlabBlock(AbstractBlock.Settings.copy(DEEPSLATE_TILES)));
DEEPSLATE_TILE_WALL = register("deepslate_tile_wall", new WallBlock(AbstractBlock.Settings.copy(DEEPSLATE_TILES)));
DEEPSLATE_BRICKS = register("deepslate_bricks", new Block(AbstractBlock.Settings.copy(COBBLED_DEEPSLATE).strength(1.5F, 6.0F).sounds(BlockSoundGroup.DEEPSLATE_BRICKS)));
DEEPSLATE_BRICK_STAIRS = register("deepslate_brick_stairs", new StairsBlock(DEEPSLATE_BRICKS.getDefaultState(), AbstractBlock.Settings.copy(DEEPSLATE_BRICKS)));
DEEPSLATE_BRICK_SLAB = register("deepslate_brick_slab", new SlabBlock(AbstractBlock.Settings.copy(DEEPSLATE_BRICKS)));
DEEPSLATE_BRICK_WALL = register("deepslate_brick_wall", new WallBlock(AbstractBlock.Settings.copy(DEEPSLATE_BRICKS)));
CHISELED_DEEPSLATE = register("chiseled_deepslate", new Block(AbstractBlock.Settings.copy(COBBLED_DEEPSLATE).strength(1.5F, 6.0F).sounds(BlockSoundGroup.DEEPSLATE_BRICKS)));
SMOOTH_BASALT = register("smooth_basalt", new Block(AbstractBlock.Settings.copy(BASALT)));
Iterator var0 = Registry.BLOCK.iterator();"""