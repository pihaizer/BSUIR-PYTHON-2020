from singleton import SingletonTemplate
import unittest

class EmptyClass(metaclass=SingletonTemplate):
    pass

class TestSingleton(unittest.TestCase):

    def test_class_only_instance(self):
        first = EmptyClass()
        second = EmptyClass()

        self.assertEqual(first, second)

    def test_saves_instance(self):
        instance = EmptyClass()
        self.assertEqual(instance, SingletonTemplate._instances[EmptyClass])


def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSingleton, 'test'))
    return suite
