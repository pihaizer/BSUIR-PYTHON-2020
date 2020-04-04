import pytest

from .. import *
from ..exceptions import *


def test_init():
    v = Vector(2, 3)
    assert v.components[0] == v[0] == 2
    assert v.components[1] == v[1] == 3


def test_eq():
    assert Vector(2, 3) == Vector(2, 3)
    assert Vector(2, 5) != Vector(2, 3)
    assert Vector(2, 3) != 5


def test_repr():
    v = Vector(2, "asd", [5, 6])
    assert str(v) == "{2, 'asd', [5, 6]}"


def test_set():
    v = Vector(2, 3)
    v[1] = 5
    assert v == Vector(2, 5)


def test_neg():
    assert Vector(2, 3, 5) == -Vector(-2, -3, -5)


def test_copy():
    v = Vector(2, 3)
    assert v.copy() == v


class TestSum:
    @pytest.mark.parametrize("test_input", [
        (Vector(2, 3), Vector(5, 6), Vector(7, 9)),
        (Vector("asd", "qwe", ""), Vector("yyy", "123", "1"), Vector("asdyyy", "qwe123", "1"))
    ])
    def test_sum(self, test_input):
        assert test_input[0] + test_input[1] == test_input[2]

    def test_sub(self):
        assert Vector(2, 3, 5) - Vector(1, 1, 1) == Vector(1, 2, 4)

    def test_invalid_types(self):
        with pytest.raises(VectorSumException):
            v = Vector(2, 3) + 5

    def test_different_components_count(self):
        with pytest.raises(VectorSumException):
            v = Vector(2, 3) + Vector(2, 3, 5)

    def test_different_components_types(self):
        with pytest.raises(VectorSumException):
            v = Vector(2, "3") + Vector(2, True)


class TestMul:
    @pytest.mark.parametrize("test_input", [
        (Vector(2, 3), 3, Vector(6, 9)),
        (Vector("asd", "qwe", "1"), 2, Vector("asdasd", "qweqwe", "11"))
    ])
    def test_mul(self, test_input):
        assert test_input[0] * test_input[1] == test_input[2]
        assert test_input[1] * test_input[0] == test_input[2]

    def test_div(self):
        assert Vector(2, 5) / 2 == Vector(1, 2.5)

    def test_invalid_type(self):
        with pytest.raises(VectorMulException):
            v = Vector(2, 3) * "asd"

    def test_scalar(self):
        assert Vector(2, 3).scalar(Vector(3, 5)) == Vector(6, 15)

    def test_scalar_invalid_type(self):
        with pytest.raises(VectorScalarException):
            v = Vector(2, 5).scalar(123)


def test_length():
    assert Vector(3, 4).length() == 5
    assert Vector(5, 12).length() == 13


def test_length_of_invalid_vector():
    with pytest.raises(VectorException):
        length = Vector(2, "asd").length()



