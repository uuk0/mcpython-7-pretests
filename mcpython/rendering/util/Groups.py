import typing

import pyglet


class OffsetBatchGroup(pyglet.graphics.Group):
    """
    A group for offsetting the rendering by 3 floats (OpenGL doubles) as in 3d space
    Can be used in batch rendering with pyglet [Until pyglet 2.0]
    """

    def __init__(
        self,
        offset: typing.Tuple[float, float, float],
        parent: pyglet.graphics.Group = None,
    ):
        super().__init__(parent)
        self.__offset = offset

        # for faster set/unsets, as pyglet decides how often this is called...
        self.__neg_offset = tuple(-e for e in offset)

    def get_offset(self):
        return self.__offset

    def set_offset(self, offset):
        self.__offset = offset
        self.__neg_offset = tuple(-e for e in offset)

    offset = property(get_offset, set_offset)

    def set_state(self):
        pyglet.gl.glTranslated(*self.__offset)

    def unset_state(self):
        pyglet.gl.glTranslated(*self.__neg_offset)
