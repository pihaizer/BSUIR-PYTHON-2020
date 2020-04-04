# A @cached decorator that caches results of functions based on args
from collections import defaultdict
from functools import wraps

def cached(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        function_name = func.__name__
        
        args_str = ','.join(map(str, args))
        kwargs_str = ','.join('{}={}'.format(k, v) for k, v in kwargs.items())
        all_args_str = ','.join([args_str, kwargs_str])

        if all_args_str in cached.func_cache[function_name]:
            return cached.func_cache[function_name][all_args_str]
        else:
            result = func(*args, **kwargs)
            cached.func_cache[function_name][all_args_str] = result
            return result
    return wrapper
cached.func_cache = defaultdict(dict)