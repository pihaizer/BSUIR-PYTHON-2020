from design_patterns.singleton import SingletonMeta
from threading import Thread

import unittest


class SomeClass(metaclass=SingletonMeta):

    def __init__(self):
        pass

    def some_method(self):
        pass


class TestSingleton(unittest.TestCase):
    instance_list = []

    def create_instance(self):
        instance = SomeClass()
        self.instance_list.append(instance)

    def test_creates_single_instance(self):
        instance1 = SomeClass()
        instance2 = SomeClass()
        self.assertIs(instance1, instance2)

    def test_creates_single_instance_with_some_threads(self):
        th1 = Thread(target=self.create_instance)
        th2 = Thread(target=self.create_instance)
        th1.start(), th2.start()
        th1.join(), th2.join()
        self.assertIs(*self.instance_list)


if __name__ == '__main__':
    unittest.main()