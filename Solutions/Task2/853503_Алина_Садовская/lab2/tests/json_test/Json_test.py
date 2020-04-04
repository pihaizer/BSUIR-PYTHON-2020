import unittest
import json
from lab2.code.json_conv.json_conv import JsonConverter


class TestJsonDump(unittest.TestCase):

    def test_int(self):
        data = 10
        self.assertEqual('10', JsonConverter.my_dumps(data))

    def test_float(self):
        data = 5.9
        self.assertEqual('5.9', JsonConverter.my_dumps(data))

    def test_none(self):
        data = None
        self.assertEqual('null', JsonConverter.my_dumps(data))

    def test_str(self):
        data = 'hello'
        self.assertEqual('\"hello\"', JsonConverter.my_dumps(data))

    def test_string(self):
        data = '\\'
        self.assertEqual('\"\\\"', JsonConverter.my_dumps(data))

    def test_tuple_str(self):
        data = ('10', '10')
        self.assertEqual('[\"10\", \"10\"]', JsonConverter.my_dumps(data))

    def test_tuple(self):
        data = (10, 10)
        self.assertEqual('[10, 10]', JsonConverter.my_dumps(data))

    def test_tuple_diff(self):
        data = (10, '10', 9.9, (5,4,), None)
        self.assertEqual('[10, \"10\", 9.9, [5, 4], null]', JsonConverter.my_dumps(data))

    def test_list(self):
        data = [10, 10]
        self.assertEqual('[10, 10]',JsonConverter.my_dumps(data))

    def test_list_str(self):
        data = ['10', '10']
        self.assertEqual('[\"10\", \"10\"]', JsonConverter.my_dumps(data))

    def test_list_diff(self):
        data = ['10', 10, 9.9, (9,)]
        self.assertEqual('[\"10\", 10, 9.9, [9]]', JsonConverter.my_dumps(data))

    def test_dict(self):
        data = {10: 10, 9: 9}
        self.assertEqual('{\"10\": 10, \"9\": 9}', JsonConverter.my_dumps(data))

    def test_dict_str(self):
        data = {'10': '10', '9': '9'}
        self.assertEqual('{\"10\": \"10\", \"9\": \"9\"}', JsonConverter.my_dumps(data))

    def test_dict_diff(self):
        data = {'10': '10', 9: '9', (10,): None}
        self.assertRaises(TypeError, lambda: JsonConverter.my_dumps(data))


class TestJsonLoad(unittest.TestCase):

    def test_int(self):
        data = 10
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_float(self):
        data = 9.9
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_none(self):
        data = None
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_str(self):
        data = 'hello'
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_tuple(self):
        data = (10, 10)
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_tuple_diff(self):
        data = ('10', 10, 9.9, (9,10), None, 110)
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_list(self):
        data = [10, 9]
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_list_diff(self):
        data = ['10', 9, 9.9, (9,9)]
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_dict(self):
        data = {10: 10, 9: 9}
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_dict_str(self):
        data = {'10': '10', '10': '9'}
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_dict_diff(self):
        data = {'10': '10', 2: '2', 3: None}
        json_data = json.dumps(data)
        self.assertEqual(json.loads(json_data), JsonConverter.my_loads(json_data))

    def test_invalid_data(self):
        json_data = 'error'
        self.assertRaises(ValueError, lambda: JsonConverter.my_loads(json_data))


if __name__ == '__main__':
    unittest.main()