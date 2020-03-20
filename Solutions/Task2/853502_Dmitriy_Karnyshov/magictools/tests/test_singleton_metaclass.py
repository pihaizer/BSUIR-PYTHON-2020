import unittest
from .. import singleton_metaclass

class TestSingletonMetaclass(unittest.TestCase):
    def setUp(self):
        class TestClass(metaclass=singleton_metaclass.SingletonMeta):
            pass
        self.instance_a = TestClass()
        self.instance_b = TestClass()

    def test_singleton_metaclass(self):
        self.assertTrue(self.instance_a == self.instance_b)