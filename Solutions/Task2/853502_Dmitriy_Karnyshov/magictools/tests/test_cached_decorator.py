import unittest
# from cached_decorator import cached
from .. import cached_decorator

class TestCachedDecorator(unittest.TestCase):
    def setUp(self):
        class Cache(dict):
            def __init__(self, *args):
                dict.__init__(self, args)
                self.sets_count = 0
                self.gets_count = 0
            
            def __getitem__(self, key):
                value = dict.__getitem__(self, key)
                self.gets_count += 1
                return value
            
            def __setitem__(self, key, value):
                dict.__setitem__(self, key, value)
                self.sets_count += 1
        self.cache = Cache()
        @cached_decorator.cached(self.cache)
        def square(x):
            return x ** 2
        self.square = square

    def test_cached_decorator(self):
        for _ in range(0, 10):
            self.square(10)
        self.assertTrue(self.cache.sets_count == 1, self.cache.gets_count == 9) 

    def test_cached_decorator_exception_occurrences(self):
        self.assertRaises(Exception, self.square('str'))