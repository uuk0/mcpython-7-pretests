import typing


class FunctionCache:
    """
    This system allows results of function calls to be cached dynamically, with the ability to invalidate the cache
    """

    @classmethod
    def of_parts(cls, *parts):
        return lambda func: cls(func, cache_key=lambda e: tuple(e[i] for i in parts))

    @classmethod
    def of_cache_key(cls, key: typing.Callable):
        return lambda func: cls(func, cache_key=key)

    def __init__(self, function: typing.Callable, cache_key=lambda e: e):
        self.function = function
        self.cache_key = cache_key

        self.cache = {}

    def __call__(self, *args):
        key = self.cache_key(args)
        if key in self.cache:
            return self.cache[key]

        return self.cache.setdefault(key, self.function(*args))

    def invalidate_cache(self):
        self.cache.clear()


class LazyOptional:
    """
    Class holding a getter method cached on call, with invalidation function, and None possibility
    [So the result is optional]

    todo: do we want to include meta information
    """

    def __init__(self, getter: typing.Callable):
        self.__getter = getter
        self.__cache = None
        self.__cache_set = False

    def get(self):
        if self.__cache_set:
            return self.__cache
        v = self.__getter()
        self.__cache_set = True
        self.__cache = v
        return v

    def invalidate(self):
        self.__cache = None
        self.__cache_set = False

    def __repr__(self):
        return f"LazyOptional(getter={self.__getter},value_set={self.__cache_set},cached={repr(self.__cache)})"

