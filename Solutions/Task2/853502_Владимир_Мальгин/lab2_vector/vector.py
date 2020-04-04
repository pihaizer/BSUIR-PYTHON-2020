from .exceptions import *


class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return '{' + str(self.components)[1:-1] + '}'

    def __getitem__(self, item):
        return self.components[item]

    def __setitem__(self, key, value):
        self.components[key] = value

    def __add__(self, other):
        if type(other) is not Vector:
            raise VectorSumException("Can't sum lab2_vector with not lab2_vector")
        if len(other.components) != len(self.components):
            raise VectorSumException("Can't sum vectors with different components count")
        result = self.copy()
        for i in range(len(self.components)):
            try:
                result.components[i] += other.components[i]
            except TypeError:
                raise VectorSumException("Invalid component types")
        return result

    def __neg__(self):
        result = self.copy()
        for i in range(self.size()):
            result[i] = -result[i]
        return result

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if type(other) is not int and type(other) is not float:
            raise VectorMulException("Can't multiply by not number")
        result = self.copy()
        for i in range(len(self.components)):
            result.components[i] *= other
        return result

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self.copy() * (1/other)

    def __eq__(self, other):
        if type(other) == Vector:
            return self.components == other.components
        return False

    def copy(self):
        result = Vector()
        result.components = self.components.copy()
        return result

    def length(self):
        result = 0
        try:
            for component in self.components:
                result += component ** 2
        except TypeError:
            raise VectorException("Can't evaluate length of such lab2_vector")
        return result ** 0.5

    def size(self):
        return len(self.components)

    def scalar(self, other):
        result = self.copy()
        try:
            for i in range(result.size()):
                result[i] *= other[i]
        except TypeError:
            raise VectorScalarException(self, other)
        return result


# if __name__ == '__main__':
#     a = Vector(3, 4, 5)
#     b = Vector("as", "bs", "qw")
#     print(a / 2)
