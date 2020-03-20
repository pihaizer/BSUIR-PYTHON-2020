import unittest
# from explosion.vector import Vector, VectorDimensionError
from .. import vector

class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.const = 10
        self.a_vector = vector.Vector(1, 2, 3, 4, 5)
        self.b_vector = vector.Vector(6, 7, 8, 9, 10)

    def test_vector_len(self):
        expected = 5
        result = len(self.a_vector)
        self.assertTrue(expected == result)

    def test_vector_equality_func(self):
        self.assertTrue(self.a_vector == vector.Vector(1, 2, 3, 4, 5))

    def test_vector_addition(self):
        expected = vector.Vector(7, 9, 11, 13, 15)
        result = self.a_vector + self.b_vector
        self.assertTrue(expected == result)

    def test_vector_subtraction(self):
        expected = vector.Vector(-5, -5, -5, -5, -5)
        result = self.a_vector - self.b_vector
        self.assertTrue(expected == result)

    def test_vector_multiplication(self):
        expected = vector.Vector(10, 20, 30, 40, 50)
        result = self.const * self.a_vector 
        self.assertTrue(expected == result)
        result = self.a_vector * self.const
        self.assertTrue(expected == result)
        expected = 130
        result = self.a_vector * self.b_vector
        self.assertTrue(expected == result)

    def test_vector_indexing(self):
        expected = 3
        result = self.a_vector[2]
        self.assertTrue(expected == result)

    def test_vector_type_error_occurrences(self):
        self.assertRaises(TypeError, lambda: self.a_vector + 5)
        self.assertRaises(TypeError, lambda: self.b_vector - 5)
        self.assertRaises(TypeError, lambda: self.a_vector * '5')
        self.assertRaises(TypeError, lambda: self.a_vector == 5)

    def test_vector_dimension_error_occurrences(self):
        self.assertRaises(vector.VectorDimensionError, lambda: self.a_vector + vector.Vector(1))
        self.assertRaises(vector.VectorDimensionError, lambda: self.b_vector - vector.Vector(1))
        self.assertRaises(vector.VectorDimensionError, lambda: self.a_vector * vector.Vector(1))
        self.assertRaises(vector.VectorDimensionError, lambda: self.a_vector == vector.Vector(1))

    def test_vector_index_error_occurrences(self):
        self.assertRaises(IndexError, lambda: self.a_vector[10])

    def test_vector_representation(self):
        expected = '(1, 2, 3, 4, 5)'
        result = repr(self.a_vector)
        self.assertTrue(expected == result)