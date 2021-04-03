import typing

import pyglet


class OffsetBatchGroup(pyglet.graphics.Group):
    def __init__(
        self, offset: typing.Tuple[int, int, int], parent: pyglet.graphics.Group = None
    ):
        super().__init__(parent)
        self.offset = offset
        self.neg_offset = tuple(-e for e in offset)

    def set_state(self):
        pyglet.gl.glTranslated(*self.offset)

    def unset_state(self):
        pyglet.gl.glTranslated(*self.neg_offset)
