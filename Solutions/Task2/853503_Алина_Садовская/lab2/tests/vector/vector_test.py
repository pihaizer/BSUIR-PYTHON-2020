import unittest
from lab2.code.vector.vector import DiffSize, Vector

class TestVector(unittest.TestCase):
    def test_init(self):
        vector = Vector(2)
        self.assertEqual(2, vector.size)
        self.assertEqual(int, vector.dtype)

    def test_init_float(self):
        arg = 10.3
        inst = lambda: Vector(arg)
        self.assertRaises(TypeError, inst)

    def test_init_list(self):
        arg = [5, 4, 2]
        vector = Vector(arg)
        self.assertSequenceEqual(arg, vector)
        self.assertEqual(len(arg), vector.size)
        self.assertEqual(int, vector.dtype)

    def test_init_neg(self):
        inst = lambda: Vector(-10)
        self.assertRaises(ValueError, inst)

    def test_init_list_diff_types(self):
        arg = [1.1, 1, 'a']
        inst = lambda: Vector(arg)
        self.assertRaises(TypeError, inst)

    def test_add(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([2] * 5)
        self.assertSequenceEqual([3] * 5, vect_1 + vect_2)

    def test_add_exp(self):
        vect_1 = Vector([1] * 1)
        vect_2 = Vector([2] * 2)
        self.assertRaises(DiffSize, lambda: vect_1 + vect_2)

    def test_sub(self):
        vect_1 = Vector([2] * 5)
        vect_2 = Vector([1] * 5)
        self.assertSequenceEqual([1] * 5, vect_1 - vect_2)

    def test_sub_exp(self):
        vect_1 = Vector([1] * 1)
        vect_2 = Vector([2] * 2)
        self.assertRaises(DiffSize, lambda: vect_1 - vect_2)

    def test_scalyar(self):
        vect_1 = Vector([2] * 5)
        vect_2 = Vector([1] * 5)
        self.assertEqual(10, vect_1.scalar_product(vect_2))

    def test_scalyar_exp_type(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector(['a'] * 5)
        self.assertRaises(TypeError, lambda: vect_1.scalar_product(vect_2))

    def test_scalyar_exp(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 1)
        self.assertRaises(DiffSize, lambda: vect_1.scalar_product(vect_2))

    def test_equal(self):
        vect_1 = Vector([1] * 5)
        vect_2 = Vector([1] * 5)
        vect_3 = Vector([1] * 1)
        self.assertEqual(True, vect_1 == vect_2)
        self.assertEqual(False, vect_1 == vect_3)

    def test_mult_scalyar(self):
        vect_1 = Vector([1] * 5)
        self.assertSequenceEqual([2] * 5, vect_1 * 2)


if __name__ == '__main__':
    unittest.main()