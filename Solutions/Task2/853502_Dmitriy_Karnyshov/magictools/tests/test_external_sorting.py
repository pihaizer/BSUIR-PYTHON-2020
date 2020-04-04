import os
import random
import time
import unittest
# from explosion.external_sorting import sort
from .. import external_sorting

class TestExternalSortingPerfomance(unittest.TestCase):
    def setUp(self):
        with open(os.getcwd() + '\\input', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(10000))
        self.startTime = time.time()

    def test_external_sorting_perfomance(self):
        external_sorting.sort(os.getcwd() + '\\input', os.getcwd() + '\\output', 1000)

    def tearDown(self):
        duration = time.time() - self.startTime
        print(f'{duration:.3f} s ...\r')
        os.remove(os.getcwd() + '\\input')
        os.remove(os.getcwd() + '\\output')

class TestExternalSortingResult(unittest.TestCase):
    def setUp(self):
        with open(os.getcwd() + '\\input', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000))

    def test_external_sorting_result(self):
        external_sorting.sort(os.getcwd() + '\\input', os.getcwd() + '\\output', 1000)
        self.assertTrue(self.file_is_sorted())

    def file_is_sorted(self):
        with open(os.getcwd() + '\\output', 'r') as f:
            first_value = f.readline()
            second_value = f.readline()
            while True:
                if second_value:
                    if int(first_value) > int(second_value):
                        return False
                    first_value = second_value
                    second_value = f.readline()
                else:
                    break
            return True

    def tearDown(self):
        os.remove(os.getcwd() + '\\input')
        os.remove(os.getcwd() + '\\output')

class TestExternalSortingErrorOccurences(unittest.TestCase):
    def setUp(self):
        with open(os.getcwd() + '\\wrong_input', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(500))
            f.write('char\n')
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(500))

    def test_external_sorting_value_error(self):
        self.assertRaises(ValueError, external_sorting.sort, os.getcwd() + '\\wrong_input', os.getcwd() + '\\wrong_output', 1000)

    def tearDown(self):
        os.remove(os.getcwd() + '\\wrong_input')