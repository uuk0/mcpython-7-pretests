import uuid

import PIL.Image
import mcpython.ProcessManager
from mcpython import shared

# The raw string, for suppressing file loading on other processes
read_image = """from mcpython import shared
image = shared.resource_locator.read_image(file)
handler.execute_on("rendering", '''BAKER.add_texture(image, reference)''', image=image, reference=reference)"""


class TextureBaker:
    class TextureReference:
        def __init__(self):
            self.id = uuid.uuid4()
            self.added = False
            self.baker = None

        def get_texture(self):
            pass

        def get_texture_group(self):
            pass

        def get_uv(self, section=(0, 0, 1, 1)):
            pass

    def __init__(self):
        self.references = {}
        self.pending_images = 0

    def add_from_file(self, file: str) -> TextureReference:
        reference = TextureBaker.TextureReference()
        self.references[reference.id] = reference
        shared.process_handler.execute_on("file_io", read_image, file=file, reference=reference)
        self.pending_images += 1
        return reference

    def add_texture(self, texture: PIL.Image.Image, reference=None) -> TextureReference:
        if reference is None:
            reference = TextureBaker.TextureReference()
            self.references[reference.id] = reference
        else:
            reference = self.references[reference.id]
        reference.baker = self

        # todo: add image to internal list

        self.pending_images -= 1
        return reference

    def bake(self):
        if self.pending_images:
            raise RuntimeError("bake called before results are in!")


BAKER = TextureBaker()
