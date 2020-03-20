import unittest
import random
import os
import time
import json
from external_sorting import sort
from json_converter import to_json, from_json, JsonFormatError
from vector import Vector, VectorDimensionError
from cached_decorator import cached
from singleton_metaclass import SingletonMeta
import coverage

class TestExternalSortingPerfomance(unittest.TestCase):
    def setUp(self):
        with open(os.getcwd() + '\\input', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(10000))
        self.startTime = time.time()

    def test_external_sorting_perfomance(self):
        sort(os.getcwd() + '\\input', os.getcwd() + '\\output', 1000)

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
        sort(os.getcwd() + '\\input', os.getcwd() + '\\output', 1000)
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
        self.assertRaises(ValueError, sort, os.getcwd() + '\\wrong_input', os.getcwd() + '\\wrong_output', 1000)

    def tearDown(self):
        os.remove(os.getcwd() + '\\wrong_input')

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
        result_string = to_json(self.test_instance)
        self.assertTrue(expected_string == result_string)

    def test_from_json_conversion(self):
        json_string = '{"b": true, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        expected_object = {"b": True, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", 
                          "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}
        result_object = from_json(json_string)
        self.assertTrue(expected_object == result_object)

    def test_from_json_conversion_error_handling(self):
        invalid_string_1 = '{"b": true, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": "a": 1, "b": 22}}'
        invalid_string_2 = '{"b": True, "l": [1, 2, 4], "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        invalid_string_3 = '{"b": true, "l": [1, 2, 4], nested: {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        invalid_string_4 = '{"b": true, "l": (1, 2, 4), "nested": {"tup": [1, [2, 3]]}, "string": "a bite of python", "t": [1, 2, 3, 4], "u": 20, "z": {"a": 1, "b": 22}}'
        self.assertRaises(JsonFormatError, from_json, invalid_string_1)
        self.assertRaises(JsonFormatError, from_json, invalid_string_2)
        self.assertRaises(JsonFormatError, from_json, invalid_string_3)
        self.assertRaises(JsonFormatError, from_json, invalid_string_4)


    def test_json_validation(self):
        json_string = to_json(self.test_instance)
        def validate_json(string):
            try:
                json.loads(string)
            except ValueError:
                return False
            return True
        self.assertTrue(validate_json(json_string))

class TestVectorClass(unittest.TestCase):
    def setUp(self):
        self.const = 10
        self.a_vector = Vector(1, 2, 3, 4, 5)
        self.b_vector = Vector(6, 7, 8, 9, 10)

    def test_vector_len(self):
        expected = 5
        result = len(self.a_vector)
        self.assertTrue(expected == result)

    def test_vector_equality_func(self):
        self.assertTrue(self.a_vector == Vector(1, 2, 3, 4, 5))

    def test_vector_addition(self):
        expected = Vector(7, 9, 11, 13, 15)
        result = self.a_vector + self.b_vector
        self.assertTrue(expected == result)

    def test_vector_subtraction(self):
        expected = Vector(-5, -5, -5, -5, -5)
        result = self.a_vector - self.b_vector
        self.assertTrue(expected == result)

    def test_vector_multiplication(self):
        expected = Vector(10, 20, 30, 40, 50)
        result = self.const * self.a_vector 
        self.assertTrue(expected == result)
        result = self.a_vector * self.const
        self.assertTrue(expected == result)
        expected = 130
        result = self.a_vector * self.b_vector
        self.assertTrue(expected == result)

    def test_vector_indexing(self):
        expected = 3
        result = self.a_vector[2]
        self.assertTrue(expected == result)

    def test_vector_type_error_occurrences(self):
        self.assertRaises(TypeError, lambda: self.a_vector + 5)
        self.assertRaises(TypeError, lambda: self.b_vector - 5)
        self.assertRaises(TypeError, lambda: self.a_vector * '5')
        self.assertRaises(TypeError, lambda: self.a_vector == 5)

    def test_vector_dimension_error_occurrences(self):
        self.assertRaises(VectorDimensionError, lambda: self.a_vector + Vector(1))
        self.assertRaises(VectorDimensionError, lambda: self.b_vector - Vector(1))
        self.assertRaises(VectorDimensionError, lambda: self.a_vector * Vector(1))
        self.assertRaises(VectorDimensionError, lambda: self.a_vector == Vector(1))

    def test_vector_index_error_occurrences(self):
        self.assertRaises(IndexError, lambda: self.a_vector[10])

    def test_vector_representation(self):
        expected = '(1, 2, 3, 4, 5)'
        result = repr(self.a_vector)
        self.assertTrue(expected == result)

class TestCachedDecorator(unittest.TestCase):
    def setUp(self):
        class Cache(dict):
            def __init__(self, *args):
                dict.__init__(self, args)
                self.sets_count = 0
                self.gets_count = 0
            
            def __getitem__(self, key):
                value = dict.__getitem__(self, key)
                self.gets_count += 1
                return value
            
            def __setitem__(self, key, value):
                dict.__setitem__(self, key, value)
                self.sets_count += 1
        self.cache = Cache()
        @cached(self.cache)
        def square(x):
            return x ** 2
        self.square = square

    def test_cached_decorator(self):
        for _ in range(0, 10):
            self.square(10)
        self.assertTrue(self.cache.sets_count == 1, self.cache.gets_count == 9) 

    def test_cached_decorator_exception_occurrences(self):
        self.assertRaises(Exception, self.square('str'))

class TestSingletonMetaclass(unittest.TestCase):
    def setUp(self):
        class TestClass(metaclass=SingletonMeta):
            pass
        self.instance_a = TestClass()
        self.instance_b = TestClass()

    def test_singleton_metaclass(self):
        self.assertTrue(self.instance_a == self.instance_b  )
