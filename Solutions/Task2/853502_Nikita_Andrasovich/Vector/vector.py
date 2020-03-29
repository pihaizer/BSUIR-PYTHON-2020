# Vector of any elements
class Vector:
    def __init__(self, *elements):
        self._elements = list()
        self._elements.extend(elements)
        self.size = len(elements)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index >= self.size:
            raise Exception(
                f"Index out of bounds (size is {self.size} and index is {index}")

        return self._elements[index]

    def __add__(self, other):
        if self.size != other.size:
            return Vector()

        newVector = Vector()
        for i in range(self.size):
            newVector.add_element(self[i]+other[i])

        return newVector

    def __sub__(self, other):
        if self.size != other.size:
            return Vector()

        newVector = Vector()
        for i in range(self.size):
            newVector.add_element(self[i]-other[i])

        return newVector

    def __mul__(self, other):
        if not isinstance(other, Vector):
            newVector = Vector()

            for i in range(self.size):
                newVector.add_element(self[i]*other)

            return newVector
        else:
            if self.size != other.size:
                return Vector()

            scalar = 0

            for i in range(self.size):
                scalar += self[i]*other[i]

            return scalar

    def __eq__(self, other):
        if self.size != other.size:
            return False

        for i in range(self.size):
            if self[i] != other[i]:
                return False
        else:
            return True

    def __str__(self):
        if self.size == 0:
            return "Vector()"

        string = f"Vector{self.size}("
        for element in self._elements:
            string += f"{element}, "

        return rreplace(string, ", ", ")", 1)

    def add_element(self, element):
        self._elements.append(element)
        self.size += 1

    def clear(self):
        self._elements.clear()
        self.size = 0


def rreplace(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)