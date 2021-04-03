import enum
import typing

import pyglet
import mcpython.rendering.block.DimensionRenderingCache


class RenderingTarget(enum.Enum):
    """
    This holds all states of rendering
    todo: extendable
    todo: allocation in ChunkSectionCache dynamic
    """

    DEFAULT = 0
    ALPHA = 1


class ChunkSectionCache:
    """
    Cache for a Chunk section to render, including one vertex list, which is updated
    internally from the block renderers
    """

    def __init__(self, position: typing.Tuple[int, int], redraw_callback: typing.Callable[["ChunkSectionCache"], None] = None):
        self.normal_vertex_buffer: typing.Optional[
            pyglet.graphics.vertexdomain.VertexList
        ] = None
        self.alpha_vertex_buffer: typing.Optional[
            pyglet.graphics.vertexdomain.VertexList
        ] = None

        self.rendering_cache: typing.Optional[
            mcpython.rendering.block.DimensionRenderingCache.DimensionRenderingCache
        ] = None

        self.vertex_count = [0, 0]  # normal, alpha

        self.position = position

        # todo: here we can do some magic for higher worlds...
        self.rendering_offset = position[0] * 16, 0, position[1] * 16

        self.redraw_callback = redraw_callback

    def setup_for_cache(
        self,
        cache: mcpython.rendering.block.DimensionRenderingCache.DimensionRenderingCache = None,
    ):
        # clean up before
        # todo: can we re-add all previous data / migrate batch -> batch?
        self.delete()

        if cache is not None: self.rendering_cache = cache

        self.normal_vertex_buffer = self.rendering_cache.create_normal_vertex_list(
            self.rendering_offset
        )
        self.alpha_vertex_buffer = self.rendering_cache.create_alpha_vertex_list(
            self.rendering_offset
        )

    def delete(self):
        if self.normal_vertex_buffer is not None:
            self.normal_vertex_buffer.delete()

        if self.alpha_vertex_buffer is not None:
            self.alpha_vertex_buffer.delete()

    def allocate_new(self, vertices: typing.Iterable[float], texture_coordinates: typing.Iterator[float], target=RenderingTarget.DEFAULT) -> int:
        # todo: something better here? [dynamic structure by lookup in list/dict/default-dict?]
        buffer = self.normal_vertex_buffer if target.value == 0 else self.alpha_vertex_buffer
        index = self.vertex_count[target.value]
        self.vertex_count[target.value] += 1

        # todo: is this correct?
        buffer.resize(index+1)
        buffer.vertices += vertices
        buffer.tex_coords += texture_coordinates

        # todo: something better!
        return index if target.value == 0 else -index-1

    def modify_existing(self, index: int, vertices: typing.Iterable[float], texture_coordinates: typing.Iterator[float]):
        pass  # todo: implement

    def deallocate(self, index: int):
        pass  # todo: implement, maybe need a whole re-draw? [This maybe by an internal flag and a redraw_if_needed call, and de-allocation scheduling, or do something fancy with indexes]

    def redraw(self, warn_on_missing_callback=True):
        """
        Redraws the data in this section using the callback given in the constructor
        Will clear the internal allocated section before re-drawing
        """

        # todo: not delete, empty by resizing?
        self.delete()
        self.setup_for_cache()

        if callable(self.redraw_callback):
            self.redraw_callback(self)

        elif warn_on_missing_callback:
            # todo: include more meta-data
            print(f"[CHUNK SECTION CACHE RENDERER][WARN] section {self.position} has no set callback, but was scheduled for redraw")
