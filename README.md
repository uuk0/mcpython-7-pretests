# mcpython-7-pretests
Repo for some tests for the 7th revision of mcpython

Started nearly 2 years after the first public release of the mcpython series


Repo for testing stuff out and writing the base systems for the real mcpython-7
This is phase-1 of the development of mcpython 7, see below for a roadmap:
1. Preparations (do research on how to do stuff, with other smaller tests) 
   [Since ~17.2.2018 public, before 1-2 years private for fundamental tests]: mostly finished by now
2. Design choices must be made: some are, some aren't
3. Write the functional code implementing the design: What we currently do?
4. Collect: What works, what not? What parts do need a revisit, which parts do work as we like them to do?
5. Write the game, collecting the results from here


Tests out currently the following stuff:
- nuitka compiler
- multiprocessing

Planned tests:
- networking
- full data-driven system (-> compiled code can still load stuff)
- custom nuitka plugin
- pre-commit-hook for formatting the code
- fast rendering
- pyglet 2.0 compatibility

Launching the game [DEV-only]
-
```shell
py launch.py
```

Building the game [DEV-only]
-
```shell
py build.py
```

WARNING: 
- builds will take some time to complete, especially on first build
- as part of the whole test phase, builds may NOT work


# API's

Data-Driven
-

- Blocks, Items, Entities (inclusive AI definitions)
- Block Models, Block States, Item Models, Entity Models, Animations (including complex ones for entities)
- recipes, tags (including gameplay tags), script-like .mcfunction files
- loot tables, world generation

Python loaded
-

Codecs for data driven system
The following codecs are arrival:
- Block Codec: codec for block types


Storage Design:
- registry tables:
  - blocks used in palettes for referencing block names, so there is only an ID, linking here
- Chunk:
  - a map chunk relative pos -> chunk data:
    - shared_palette: a palette of size u2 with ref size ceil(log2(size)), maybe add global palette and special ref from here?
    - sectors: a list of the following structures:
      - u2 cy: the y//16 coord this section starts 
      - u2 palette size followed by palette entries 
      - the world, as an array of 16\*16\*16 entries, starting with 0 for local and 1 for shared, followed by needed
        bits for reference

