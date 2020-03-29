import fileMergeSort
import unittest
import random
import os


class TestSort(unittest.TestCase):

    def tearDown(self):
        if os.path.exists("testOut.txt"):
            os.remove("testOut.txt")

        if os.path.exists("test_rundom_numbers.txt"):
            os.remove("test_rundom_numbers.txt")

    def test_small_set(self):
        fileMergeSort.sort("testNum.txt", "testOut.txt")

        with open("testOut.txt", 'r') as output_file:
            sorted = output_file.read().replace("\n", " ").strip()
            self.assertEqual(sorted, "-5 1 2 5 7 10 13 19 20 32")

    def test_random_set(self):
        set = list()

        with open("test_rundom_numbers.txt", 'w') as file:
            for _ in range(500):
                number = random.randint(-1000000, 1000000)

                set.append(number)
                file.writelines('{}\n'.format(number))

        set.sort()
        fileMergeSort.sort("test_rundom_numbers.txt", "testOut.txt")

        with open("testOut.txt", 'r') as output_file:
            sorted = output_file.read().replace("\n", " ").strip()
            self.assertEqual(sorted, " ".join(map(str, set)))


def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSort, 'test'))
    return suite
