import typing
import uuid

import PIL.Image
import pyglet

from mcpython import shared

# The raw string, for suppressing file loading on other processes
# WARNING: modify only when you know whats possible
# todo: make fail-safe
read_image = """from mcpython import shared
image = shared.resource_locator.read_image(file)
handler.execute_on("rendering", '''BAKER.add_texture(image, reference, decrease_counter=True)''', image=image, reference=reference)"""


class TextureBaker:
    """
    Baker for baking textures into one big atlas, and loading references to it
    """

    class TextureReference:
        """
        Reference to a texture in the atlas
        WARNING: the underlying atlas may not be baked immediately
        Use the added flag to check for addition to the atlas
        """

        def __init__(self):
            self.id = uuid.uuid4()  # this may be needed, there might be a better bake
            self.added = False
            self.baker: typing.Optional["TextureBaker"] = None
            self.position: typing.Optional[
                typing.Tuple[float, float, float, float]
            ] = None

        def get_texture(self) -> pyglet.image.Texture:
            """
            Returns the underlying texture loaded into pyglet
            """
            assert self.added, "texture atlas must be baked before referencing it"
            return self.baker.internal_texture

        def get_texture_group(self) -> pyglet.graphics.TextureGroup:
            """
            Returns the texture group shared across the texture baker instance
            """
            assert self.added, "texture atlas must be baked before referencing it"
            return self.baker.internal_texture_group

        def get_uv(
            self, section=(0, 0, 1, 1)
        ) -> typing.Tuple[float, float, float, float]:
            """
            Returns the UV's for this texture section on the texture atlas
            :param section: the section of the texture
            """
            assert self.added, "texture atlas must be baked before referencing it"
            ax, ay, bx, by = section
            x, y = self.position
            sx, sy = self.baker.grid_size
            # todo: is this correct and the best way?
            # todo: cache & invalidate by last bake cycle
            return (
                x / sx + ax / sx,
                y / sy + ay / sy,
                (x + 1) / sx - (1 - bx) / sx,
                (y + 1) / sy - (1 - by) / sy,
            )

    def __init__(self):
        self.references = {}

        # The pending image counter; DON'T TOUCH WHEN YOU DON'T KNOW WHAT YOU ARE DOING. MAY BREAK EVERYTHING!
        # todo: maybe property() with only getter?
        self.pending_images = 0

        # a set of all pending textures for baking; Over this set, with popping is iterated during bake
        # if this is non-empty, schedule a bake when possible
        # It is dynamic and allows during baking image addition
        self.pending_textures = set()

        self.internal_texture = None
        self.internal_texture_group = None

        self.grid_size = (0, 0)

    def add_from_file(self, file: str) -> TextureReference:
        """
        Wrapper of add_texture() around the IO process for later fast-loading
        WARNING: this is the lazy-est variant. Until load, it will take a while
            (send request to IO process, load file, send data back to this process, add to atlas, and bake)
        :param file: the file to load
        :return: the reference
        """

        reference = TextureBaker.TextureReference()
        self.references[reference.id] = reference
        shared.process_handler.execute_on(
            "file_io", read_image, file=file, reference=reference
        )
        self.pending_images += 1
        return reference

    def add_texture(
        self, texture: PIL.Image.Image, reference=None, decrease_counter=False
    ) -> TextureReference:
        """
        Adds a texture into the internal texture array
        :param texture: the texture
        :param reference: a existing reference, for re-use purposes, use returned reference where possible,
            as we might need to create a new reference anyway.
        :param decrease_counter: internal only; Will decrease the internal counter
        :return: the texture reference
        """

        if reference is None:
            reference = TextureBaker.TextureReference()
            self.references[reference.id] = reference
        else:
            reference = self.references[reference.id]
            reference.added = False
        reference.baker = self
        self.pending_textures.add((reference.id, texture))

        if decrease_counter:
            self.pending_images -= 1
        return reference

    def bake(self):
        """
        Bakes the atlas
        :raise RuntimeError: when there are pending texture loads scheduled on the IO process
        """

        if self.pending_images:
            raise RuntimeError("bake called before results are in!")

        while len(self.pending_textures) > 0:
            ref_id, texture = self.pending_textures.pop()

            # todo: work here...


BAKER = TextureBaker()
