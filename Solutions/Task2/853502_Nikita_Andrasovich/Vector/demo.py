from vector import Vector
import unittest
import tests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.tests_suite())
    return suite


if __name__ == '__main__':
    tests_result = unittest.TextTestRunner(verbosity=0).run(suite())

    if not tests_result.wasSuccessful():
        exit(1)

    v = Vector(1, 22, 3)
    v2 = Vector(9, 8, 7)

    print(f"First vector: {v}")
    print(f"Second vector: {v2}", end="\n\n")

    print(f"Are vectors equal: {v==v2}", end="\n\n")

    print(f"Vector sum: {v+v2}")
    print(f"Vector sub: {v-v2}", end="\n\n")
    print(f"First vector mul by 2: {v*2}")
    print(f"Scalar vector multiplication: {v*v2}", end="\n\n")
