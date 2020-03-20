import json
import unittest
# from explosion.json_converter import to_json, from_json, JsonFormatError
from .. import json_converter

class TestJsonConverter(unittest.TestCase):
    def setUp(self):
        class NestedClass():
            tup = (1, (2, 3))
        class TestClass():
            string = 'a bite of python'
            u = 20
            l = [1, 2, 4]
            t = (1, 2, 3, 4)
            z = {'a': 1, 'b': 22}
            b = True
            nested = NestedClass()
        self.test_instance = TestClass()

    def test_to_json_conversion(self):
        expected_string = '{"b": true, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        result_string = json_converter.to_json(self.test_instance)
        self.assertTrue(expected_string == result_string)

    def test_from_json_conversion(self):
        json_string = '{"b": true, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        expected_object = {"b": True, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", 
                          "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}
        result_object = json_converter.from_json(json_string)
        self.assertTrue(expected_object == result_object)

    def test_from_json_conversion_error_handling(self):
        invalid_string_1 = '{"b": true, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": "a": 1, "b": 22}}'
        invalid_string_2 = '{"b": True, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        invalid_string_3 = '{"b": true, "l": [1, 2, 4], nested: {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        invalid_string_4 = '{"b": true, "l": (1, 2, 4), "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        self.assertRaises(json_converter.JsonFormatError, json_converter.from_json, invalid_string_1)
        self.assertRaises(json_converter.JsonFormatError, json_converter.from_json, invalid_string_2)
        self.assertRaises(json_converter.JsonFormatError, json_converter.from_json, invalid_string_3)
        self.assertRaises(json_converter.JsonFormatError, json_converter.from_json, invalid_string_4)

    def test_json_validation(self):
        json_string = json_converter.to_json(self.test_instance)
        def validate_json(string):
            try:
                json.loads(string)
            except ValueError:
                return False
            return True
        self.assertTrue(validate_json(json_string))