funcs: dict = None


def cached(func):
    global funcs
    if funcs is None:
        funcs = {}
    if func not in funcs.keys():
        funcs[func] = {}

    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) == 0:
            return func(args, kwargs), False

        args_hash = hash((args, tuple(kwargs.items())))
        args_dict: dict = funcs[func]
        # if args_dict[args_hash] is None:
        if args_hash not in args_dict.keys():
            return_value = func(*args, **kwargs)
            args_dict[args_hash] = [(args, kwargs, return_value)]
            return return_value, False
        else:
            for item in args_dict[args_hash]:
                if item[0] == args and item[1] == kwargs:
                    return item[2], True
            return_value = func(*args, **kwargs)
            args_dict[args_hash].append((args, kwargs, return_value))
            return return_value, False

    return wrapper


class Test:
    def __init__(self, a):
        self.a = a


@cached
def test(a, *args, **kwargs):
    return a, *args, kwargs


if __name__ == '__main__':
    c = Test("123")
    print(test(c, 1))
    print(test(c, 1))
    print(test(c, 1))
