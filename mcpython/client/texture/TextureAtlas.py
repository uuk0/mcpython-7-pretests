import typing

import PIL.Image
import pyglet

from mcpython import shared


async def lookup_resource(side, file: str):
    f = shared.local+"/tmp."+file.split(".")[-1]
    shared.resource_manager.read_to_file(file, f)

    import PIL.Image

    return PIL.Image.open(f)


class TextureAtlas:
    def __init__(self):
        self.foundation_image = PIL.Image.new("RGBA", (16*32, 16*32), (0, 0, 0, 0))
        self.file2position = {}
        self.cursor = 0, 0
        self.entries = 32, 32

        self.loaded_pyglet_image = None

    def add_texture(self, file_name: str, image: PIL.Image.Image) -> typing.Tuple[int, int]:
        if file_name in self.file2position: return self.file2position[file_name]

        x, y = self.cursor
        self.foundation_image.paste(image, (x*16, y*16))
        pos = self.file2position[file_name] = x, self.entries[1]-y-1

        x += 1
        if x >= self.entries[0]:
            x = 0
            y += 1

            if y >= self.entries[1]:
                raise RuntimeError("ImageSpaceOutOfBounds")

        self.cursor = x, y

        return pos

    async def async_add_texture(self, file_name: str):
        if file_name in self.file2position: return self.file2position[file_name]

        image = await shared.async_side_instance.sided_task_manager.invokeOn("data_processing", lookup_resource, file_name)
        return self.add_texture(file_name, image)

    def bake(self):
        self.foundation_image.save(shared.local+"/texture_atlas.png")
        self.loaded_pyglet_image = pyglet.image.load(shared.local+"/texture_atlas.png").get_texture()

    def clean(self):
        self.foundation_image = PIL.Image.new("RGBA", (16 * 32, 16 * 32), (0, 0, 0, 0))
        self.file2position.clear()
        self.cursor = 0, 0
        self.loaded_pyglet_image = None

