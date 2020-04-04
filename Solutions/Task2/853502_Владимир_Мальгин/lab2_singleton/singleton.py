singletons: dict = {}


def singleton(Cls):
    class NewCls(object):
        instance = None

        def __new__(cls, *args, **kwargs):
            if Cls not in singletons.keys():
                instance = Cls(*args, **kwargs)
                singletons[Cls] = instance
                return instance
            else:
                return singletons[Cls]

        def __getattr__(self, name):
            return getattr(self.instance, name)

        def __setattr__(self, name, value):
            return setattr(self.instance, name, value)

    return NewCls


@singleton
class SomeClass:
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    a = SomeClass("123")
    print(a)
    b = SomeClass("123")
    print(a)
