

class DimensionRenderingCache:
    """
    Cache holding all the rendering information for a dimension
    Multiple info's may co-exist on one client for multi-dimension rendering, overlay rendering,
    gui rendering, fast dimension travel, ...
    current pending ChunkSectionCache's may be stored here, but they should be mainly stored in their
    respective Chunk instance

    todo: implement
    """

