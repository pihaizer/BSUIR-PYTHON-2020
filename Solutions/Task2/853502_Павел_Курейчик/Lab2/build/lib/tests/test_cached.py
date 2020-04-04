from custom_decorators.cached import cached, MemoizationError
from time import time, sleep

import unittest


def factorial(n, *args, **kwargs):
    if n < 0:
        return float('nan')
    elif n < 2:
        return 1
    else:
        res = 1
        for value in range(2, int(n) + 1):
            res *= value
    sleep(1)
    return res


class TestCached(unittest.TestCase):

    def test_equal_function_result(self):
        self.assertEqual(factorial(5), cached(factorial)(5))

    def test_equal_result_using_args_and_kwargs(self):
        self.assertEqual(factorial(6, 1, 2, 3, m=3), cached(factorial)(6, 1, 2, 3, m=3))

    def test_cached_works_faster(self):
        cached_fact = cached(factorial)
        start = time()
        cached_fact(1000)
        raw_time = time() - start
        start = time()
        cached_fact(1000)
        cached_time = time() - start
        self.assertGreater(raw_time, cached_time)

    def test_unhashable_args(self):
        with self.assertRaises(MemoizationError):
            cached(factorial)(111, [1, 3], key=[3, 2, 2])


if __name__ == '__main__':
    unittest.main()
