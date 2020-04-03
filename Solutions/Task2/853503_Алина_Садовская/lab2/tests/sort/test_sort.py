import unittest
import random
from lab2.code.sort_in_memory.sort import MergeSort, NotNumber


class TestSort(unittest.TestCase):
    def test_sorting(self):
        input_file = "numbers.txt"
        output_file = "number_sort.txt"
        with open(input_file, 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))

        MergeSort(input_file, output_file)

        num_count = 0
        prev_num = 0
        total = 1000000
        with open(output_file) as fp:
            for line in fp:
                next_num = int(line)
                if num_count > 0:
                    self.assertTrue(next_num >= prev_num)
                num_count += 1
                prev_num = next_num
        self.assertEqual(num_count, total)


if __name__ == '__main__':
    unittest.main()