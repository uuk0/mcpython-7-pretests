import mcpython.util.lazy


@mcpython.util.lazy.FunctionCache
def normalize(vector):
    return tuple(round(x) for x in vector)


@mcpython.util.lazy.FunctionCache.of_cache_key(lambda e: (e[0], e[-1]))
def get_chunk_pos_of(vector):
    return normalize((vector[0] // 16, vector[-1] // 16))

