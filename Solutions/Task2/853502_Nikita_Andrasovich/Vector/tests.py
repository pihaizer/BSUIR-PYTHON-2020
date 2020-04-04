from vector import Vector
import unittest


class TestVector(unittest.TestCase):

    def test_add(self):
        vector1 = Vector(10, 5)
        vector2 = Vector(3, 20)

        sum = vector1+vector2
        self.assertEqual(sum, Vector(13, 25))

    def test_sub(self):
        vector1 = Vector(5, 6)
        vector2 = Vector(2, 2)

        sub = vector1-vector2
        self.assertEqual(sub, Vector(3, 4))

    def test_mul_scalar(self):
        vector1 = Vector(13, 65, 4.5)
        vector2 = Vector(2, 22.3, 3)

        mul = vector1*vector2
        self.assertEqual(mul, 1489)

    def test_mul_by_const(self):
        vector = Vector(10, 20, "AB")

        mul = vector*2
        self.assertEqual(mul, Vector(20, 40, "ABAB"))

    def test_len(self):
        vector = Vector(3, 53, False, None, "Hello")
        self.assertEqual(len(vector), 5)

    def test_clear(self):
        vector = Vector(3, 53, False, None, "Hello")
        vector.clear()

        self.assertEqual(len(vector), 0)

    def test_string_representation(self):
        vector = Vector(3, 53, False)

        self.assertEqual(str(vector), "Vector3(3, 53, False)")

    def test_equality(self):
        vector1 = Vector(3, 53, False)
        vector2 = Vector(3, 53, False)

        self.assertTrue(vector1 == vector2)

        vector2.add_element(5)
        self.assertFalse(vector1 == vector2)

    def test_get_by_index(self):
        vector = Vector(43, 12, 56)
        self.assertEqual(vector[1], 12)

    def test_index_out_of_bounds(self):
        vector = Vector(43, 12, 56)

        with self.assertRaises(Exception):
            vector[4]


def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVector, 'test'))
    return suite
