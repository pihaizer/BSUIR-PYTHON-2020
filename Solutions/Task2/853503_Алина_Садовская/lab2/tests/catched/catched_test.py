import unittest
from lab2.code.catched.catched import cached


class TestCached(unittest.TestCase):
    def test(self):

        @cached
        def kvadrat(x):
            return x*x

        arg = 5
        result_1 = kvadrat(arg)
        arg = -10
        result_2 = kvadrat(arg)

        self.assertIs(25, result_1)
        self.assertIs(100, result_2)


if __name__ == '__main__':
    unittest.main()