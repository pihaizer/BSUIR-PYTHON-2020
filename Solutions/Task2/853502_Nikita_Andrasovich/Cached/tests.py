from cachedDecorator import cached
import unittest
import time


def long_calculation(some_arg, calculation_time):
    time.sleep(calculation_time)
    return some_arg


@cached
def addition(first, second):
    return first + second


class TestParse(unittest.TestCase):

    def test_faster_cached(self):
        t0 = time.time()
        for _ in range(10):
            long_calculation("argument", 0.005)
        t1 = time.time()

        not_cached_time = t1-t0

        t0 = time.time()
        for _ in range(10):
            cached(long_calculation("argument", 0.005))
        t1 = time.time()

        cached_time = t1-t0

        # At least two times faster
        self.assertLess(cached_time/2, not_cached_time)

    def test_save_in_cache(self):
        addition(2,2)
        self.assertTrue("addition" in cached.func_cache)

    def test_known_result_cache(self):
        addition("ab","cd")
        self.assertEqual("abcd", cached.func_cache["addition"]["ab,cd,"])


def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestParse, 'test'))
    return suite
