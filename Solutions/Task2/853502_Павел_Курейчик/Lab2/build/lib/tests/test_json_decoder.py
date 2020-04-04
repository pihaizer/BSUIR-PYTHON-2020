from jsonformatter.decoder import from_json
from jsonformatter.decoder import JSONDecoderError

from json import loads
import unittest


class TestDecoder(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(loads('true'), from_json('true'))

    def test_none(self):
        self.assertEqual(loads('null'), from_json('null'))

    def test_string(self):
        json_str = '"str1\\tstr2\\nstr3"'
        self.assertEqual(loads(json_str), from_json(json_str))

    def test_integer(self):
        self.assertEqual(loads('13'), from_json('13'))

    def test_float(self):
        self.assertEqual(loads('12e-4'), from_json('12e-4'))

    def test_infinity(self):
        self.assertEqual(float('-inf'), from_json('-Infinity'))

    def test_array(self):
        json_arr = '[11.1, "str", null, false, [Infinity, [[]]], {"a": 1, "b": [1, 2, 3]}]'
        self.assertEqual(loads(json_arr), from_json(json_arr))

    def test_object(self):
        jsob_obj = '{"a": {"b": "123"}, "2": ["str1", "str2", true], "3": [1, [2, null]]}'
        self.assertEqual(loads(jsob_obj), from_json(jsob_obj))

    def test_wrong_object_keys(self):
        with self.assertRaises(JSONDecoderError):
            from_json('{1: "str", 2: null}')

    def test_wrong_json_str(self):
        with self.assertRaises(JSONDecoderError):
            obj = '("str1", "str2", 3)'
            from_json(obj)


if __name__ == '__main__':
    unittest.main()
