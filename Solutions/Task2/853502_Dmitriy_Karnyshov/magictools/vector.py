class VectorDimensionError(Exception):
    pass

class Vector:
    def __init__(self, *components):
        self.dim = len(components)
        self.components = components

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                return Vector(*[a + b for (a, b) in zip(self.components, other.components)])
            else:
                raise VectorDimensionError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                return Vector(*[a - b for (a, b) in zip(self.components, other.components)])
            else:
                raise VectorDimensionError
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if self.dim == other.dim:
                return sum([a * b for (a, b) in zip(self.components, other.components)])
            else:
                raise VectorDimensionError
        else:
            raise TypeError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                return self.components == other.components
            else:
                raise VectorDimensionError
        else:
            raise TypeError
    
    def __getitem__(self, index):
        if index < len(self.components):
            return self.components[index]
        raise IndexError

    def __repr__(self):
        return repr(self.components)