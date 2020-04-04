from functools import wraps

def cached(cache: dict):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # checking if result is cached
            nonkeyed_args = tuple(repr(args))
            keyed_args = (tuple(repr(kwargs.keys())), tuple(repr(kwargs.values())))
            cache_key = hash((nonkeyed_args, keyed_args))
            if cache_key in cache.keys():
                return cache[cache_key]
            # calling wrapped function
            try:
                result = function(*args, **kwargs)
            except Exception:
                return
            # caching obtained result
            if result != None:
                cache[cache_key] = result
            return result
        return wrapper
    return decorator