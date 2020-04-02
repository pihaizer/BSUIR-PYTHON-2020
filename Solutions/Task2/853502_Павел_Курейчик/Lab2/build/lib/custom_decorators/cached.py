import functools


class MemoizationError(TypeError):
    def __init__(self, msg):
        super().__init__(f"{msg}")


def cached(func):
    """Use cached value or calculate and store the result in the cache."""

    cache = {}

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            signature = (func, args, tuple(kwargs.items()))
            if signature not in cache:
                cache[signature] = func(*args, **kwargs)
        except TypeError as err:
            error_msg = str(err) + ', caching is impossible.'
            raise MemoizationError(error_msg) from None
        return cache[signature]

    return wrapped

