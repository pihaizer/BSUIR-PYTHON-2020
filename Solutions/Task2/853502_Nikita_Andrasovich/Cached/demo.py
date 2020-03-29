from cachedDecorator import cached
import unittest
import tests
import time

@cached
def long_calculation_cached(some_arg, calculation_time):
    time.sleep(calculation_time)
    return some_arg


def long_calculation(some_arg, calculation_time):
    time.sleep(calculation_time)
    return some_arg


def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.tests_suite())
    return suite


if __name__ == '__main__':
    tests_result = unittest.TextTestRunner(verbosity=0).run(suite())

    if not tests_result.wasSuccessful():
        exit(1)

    print("Without @cached:")

    t0 = time.time()
    for _ in range(10):
        long_calculation("argument", 0.05)
    t1 = time.time()
    print(t1-t0, end="\n\n")

    print("With @cached:")

    t2 = time.time()
    for _ in range(10):
        long_calculation_cached("argument", 0.05)
    t3 = time.time()
    print(t3-t2, end="\n\n")
