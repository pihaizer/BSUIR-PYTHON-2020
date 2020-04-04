import pytest
from lab2_cached.cached_decorator import cached


class SomeClass:
    def __init__(self, a):
        self.a = a


class_instance = SomeClass("123")


@cached
def some_func(*args):
    return args


@pytest.mark.parametrize("test_args", [
    ("123", False),
    (123, False),
    (class_instance, False),
    ("123", True),
    (class_instance, True),
    (123, True),
    ("123", True)
])
def test_cached_args(test_args):
    args = test_args[:-1]
    must_be_cached = test_args[-1]
    result = some_func(*args)
    assert args == result[0]
    if must_be_cached:
        assert result[1] is True
    else:
        assert result[1] is False