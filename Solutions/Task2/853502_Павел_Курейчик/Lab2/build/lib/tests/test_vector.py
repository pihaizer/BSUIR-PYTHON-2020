from linalg.vector import Vector

import unittest


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector = Vector(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    def test_equal(self):
        self.assertEqual(self.vector, Vector(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_inequality_with_vector_by_values(self):
        self.assertNotEqual(self.vector, Vector(10, 2))

    def test_inequality_with_vector_by_dimension(self):
        self.assertNotEqual(self.vector, Vector(7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_inequality_with_not_vector(self):
        self.assertNotEqual(self.vector, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_negation(self):
        self.assertEqual(-self.vector, Vector(10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10))

    def test_vector_add(self):
        vector2 = Vector(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        result_vector = Vector(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
        self.assertEqual(self.vector + vector2, result_vector)

    def test_scalar_add(self):
        a = 5
        result_vector = Vector(10, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(self.vector + a, result_vector)

    def test_scalar_iadd(self):
        self.vector += 5
        result_vector = Vector(10, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(self.vector, result_vector)

    def test_vector_sub(self):
        vector2 = Vector(10, 2, 2, 3, 3, 4, 4, 5, 5, 10, 20)
        result_vector = Vector(10, -1, 0, 0, 1, 1, 2, 2, 3, -1, -10)
        self.assertEqual(self.vector - vector2, result_vector)

    def test_scalar_rsub(self):
        a = 1
        result_vector = Vector(10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9)
        self.assertEqual(a - self.vector, result_vector)

    def test_vector_isub(self):
        self.vector -= Vector(10, 2, 2, 3, 3, 4, 4, 5, 5, 10, 20)
        result_vector = Vector(10, -1, 0, 0, 1, 1, 2, 2, 3, -1, -10)
        self.assertEqual(self.vector, result_vector)

    def test_scalar_product(self):
        vector2 = Vector(10, 2, 2, 2, 2, 2, 5, 5, 5, 0, 0)
        self.assertEqual(self.vector * vector2, 135)

    def test_scalar_rmul(self):
        a = 2
        result_vector = Vector(10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
        self.assertEqual(a * self.vector, result_vector)

    def test_vector_norm(self):
        self.assertEqual(round(self.vector.norm(), 3), 19.621)

    def test_index_access(self):
        self.assertEqual(1, self.vector[0])

    def test_length(self):
        self.assertEqual(10, len(self.vector))

    def test_to_str(self):
        self.assertEqual('<1, 2, 3, 4, 5, 6, 7, 8, 9, 10>', str(self.vector))

    def test_str_repr(self):
        self.assertEqual('[1, <1, 2, 3, 4, 5, 6, 7, 8, 9, 10>]', str([1, self.vector]))

    def test_different_lengths_for_sum(self):
        with self.assertRaises(ValueError):
            self.vector + Vector(5)

    def test_different_lengths_for_sub(self):
        with self.assertRaises(ValueError):
            self.vector - Vector(3, *[5, 15, 91])

    def test_wrong_type_for_mul(self):
        with self.assertRaises(ValueError):
            a = self.vector * [1, 2, 3]

    def test_wrong_type_for_add(self):
        with self.assertRaises(ValueError):
            a = self.vector + [1, 2, 3]

    def test_wrong_type_init(self):
        with self.assertRaises(ValueError):
            vector = Vector(3, 'qwe', 3, 5.3)

    def test_modification_with_wrong_value(self):
        with self.assertRaises(ValueError):
            self.vector[0] = Vector(1)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            a = self.vector[100]


if __name__ == '__main__':
    unittest.main()
