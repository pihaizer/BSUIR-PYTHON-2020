import unittest
from lab2.code.singleton.singleton import Singleton, SimpleSingleton, SingletonWithValue


class TestSingleton(unittest.TestCase):
    def test_ref(self):
        first_object = SimpleSingleton()
        second_object = SimpleSingleton()
        self.assertIs(first_object, second_object)

    def test_ref_param(self):
        first_object = SingletonWithValue(1)
        second_object = SingletonWithValue(2)
        self.assertIs(first_object, second_object)
        self.assertEqual(second_object.value, 1)


if __name__ == '__main__':
    unittest.main()
