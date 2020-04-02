from external_sort.merge_sort import sort
from os.path import join
import tempfile
import random

import unittest


class TestExternalSort(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.gettempdir()
        self.input_path = join(self.tempdir, 'input.txt')
        self.output_path = join(self.tempdir, 'output.txt')

    def write_data(self, data, path):
        with open(path, 'w') as f:
            f.write(' '.join(str(val) for val in data))

    def read_data(self, path):
        with open(path, 'r') as f:
            return [int(val) for val in f.read().split()]

    def get_result(self, input_data, run_size):
        self.write_data(input_data, self.input_path)
        sort(self.input_path, run_size, self.output_path)
        return self.read_data(self.output_path)

    def test_small_file(self):
        input_data = [-23, 44, 88, 0, -431, 55, 90, 33, 1, 1, 1, 20, -1, +3]
        sorted_data = sorted(input_data)
        output_data = self.get_result(input_data, 5)
        self.assertEqual(sorted_data, output_data)

    def test_big_file(self):
        input_data = [random.randint(-10000, 10000) for _ in range(500000)]
        sorted_data = sorted(input_data)
        output_data = self.get_result(input_data, 100)
        self.assertEqual(sorted_data, output_data)

    def test_empty_file(self):
        output_data = self.get_result([], 10)
        self.assertEqual([], output_data)

    def test_big_run_size(self):
        input_data = [+123, -5, 0, 0, 431, 999, -17]
        sorted_data = sorted(input_data)
        output_data = self.get_result(input_data, 30)
        self.assertEqual(sorted_data, output_data)

    def test_wrong_run_size(self):
        with self.assertRaises(ValueError):
            self.get_result([767, 32, -20], 1)

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            self.get_result(['a', 123, 99], 2)


if __name__ == '__main__':
    unittest.main()