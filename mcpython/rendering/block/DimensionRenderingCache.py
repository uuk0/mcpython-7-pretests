import typing

import pyglet

import mcpython.rendering.util.OffsetBatchGroup


class DimensionRenderingCache:
    """
    Cache holding all the rendering information for a dimension
    Multiple info's may co-exist on one client for multi-dimension rendering, overlay rendering,
    gui rendering, fast dimension travel, ...
    current pending ChunkSectionCache's may be stored here, but they should be mainly stored in their
    respective Chunk instance

    This should hold the pyglet batch for the system, from which vertex lists are dynamically created

    todo: implement
    """

    def __init__(self):
        self.normal_batch = pyglet.graphics.Batch()
        self.alpha_batch = pyglet.graphics.Batch()

    def create_normal_vertex_list(
        self, offset: typing.Tuple[int, int, int], group: pyglet.graphics.Group = None
    ) -> pyglet.graphics.vertexdomain.VertexList:
        # this is magic... todo: migrate from Quads to triangles, as quars are not as optimal in some cases
        return self.normal_batch.add(
            0,
            pyglet.gl.GL_QUADS,
            mcpython.rendering.util.OffsetBatchGroup.OffsetBatchGroup(offset, group),
            ("v3d", tuple()),
            ("t2d", tuple()),
        )

    def create_alpha_vertex_list(
        self, offset: typing.Tuple[int, int, int], group: pyglet.graphics.Group = None
    ) -> pyglet.graphics.vertexdomain.VertexList:
        # this is magic... todo: migrate from Quads to triangles, as quars are not as optimal in some cases
        return self.alpha_batch.add(
            0,
            pyglet.gl.GL_QUADS,
            mcpython.rendering.util.OffsetBatchGroup.OffsetBatchGroup(offset, group),
            ("v3d", tuple()),
            ("t2d", tuple()),
        )
