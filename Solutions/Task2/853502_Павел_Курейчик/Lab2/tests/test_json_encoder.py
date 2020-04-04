from jsonformatter.encoder import to_json

from json import dumps
import unittest


class TestEncoder(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(dumps(True), to_json(True))

    def test_none(self):
        self.assertEqual(dumps(None), to_json(None))

    def test_string(self):
        self.assertEqual(dumps('str1\tstr2\nstr3'), to_json('str1\tstr2\nstr3'))

    def test_integer(self):
        self.assertEqual(dumps(2300), to_json(2300))

    def test_float(self):
        self.assertEqual(dumps(23.431), to_json(23.431))

    def test_nan(self):
        self.assertEqual(dumps(float('nan')), to_json(float('nan')))

    def test_infinity(self):
        self.assertEqual(dumps(float('inf')), to_json(float('inf')))

    def test_tuple(self):
        obj = (1, 'string', [99, (123, 321)], False)
        self.assertEqual(dumps(obj), to_json(obj))

    def test_list(self):
        obj = ['escape', (12, ), None, [12, 12.91, ['qwe', 'asd', 'zxc', [[]]]]]
        self.assertEqual(dumps(obj), to_json(obj))

    def test_dict(self):
        obj = {'a': {'b': 'bbb'}, 2: ['str1', 'str2', None], 3: (1, [2, ()])}
        self.assertEqual(dumps(obj), to_json(obj))

    def test_wrong_dict(self):
        with self.assertRaises(TypeError):
            to_json({(1, 2): 'str', 44: 'qwe'})

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            obj = unittest.TestCase()
            to_json(obj)


if __name__ == '__main__':
    unittest.main()
