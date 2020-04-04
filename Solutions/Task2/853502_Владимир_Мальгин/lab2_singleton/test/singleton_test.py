from lab2_singleton.singleton import singleton


@singleton
class SomeClass1:
    pass


@singleton
class SomeClass2:
    pass


def test_singularity():
    a = SomeClass1()
    b = SomeClass1()
    c = SomeClass1()
    assert a == b == c


def test_different_classes():
    a = SomeClass1()
    b = SomeClass2()
    assert a != b
