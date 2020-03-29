import tests
import unittest
import fileMergeSort


def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.tests_suite())
    return suite


if __name__ == '__main__':
    tests_result = unittest.TextTestRunner(verbosity=0).run(suite())

    if not tests_result.wasSuccessful():
        exit(1)

    fileMergeSort.sort("numbers.txt", "sorted.txt")
