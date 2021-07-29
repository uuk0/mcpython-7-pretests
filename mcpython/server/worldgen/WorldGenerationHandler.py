import mcpython.server.worldgen.ChunkGenerator


class WorldGenerationHandler:
    def __init__(self):
        self.chunk_generator = {}

    def new_chunk_generator(self, name: str):
        return self.chunk_generator.setdefault(
            name, mcpython.server.worldgen.ChunkGenerator.ChunkGenerator(name)
        )
