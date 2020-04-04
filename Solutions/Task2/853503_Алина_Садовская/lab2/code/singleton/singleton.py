class Singleton(type):
    exemplar = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.exemplar:
            cls.exemplar[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.exemplar[cls]


class SimpleSingleton(metaclass=Singleton):
    pass


class SingletonWithValue(metaclass=Singleton):
    def __init__(self, value):
        self.value = value

ref_1 = SimpleSingleton()
ref_2 = SimpleSingleton()

print(ref_1)
print(ref_2)