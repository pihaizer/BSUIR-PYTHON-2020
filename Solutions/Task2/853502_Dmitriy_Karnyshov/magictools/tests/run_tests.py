import unittest
from . import test_cached_decorator
from . import test_external_sorting
from . import test_json_converter
from . import test_singleton_metaclass
from . import test_vector_class

def main():
    suite_cached = unittest.TestLoader().loadTestsFromModule(test_cached_decorator)
    suite_sort = unittest.TestLoader().loadTestsFromModule(test_external_sorting)
    suite_json = unittest.TestLoader().loadTestsFromModule(test_json_converter)
    suite_singleton = unittest.TestLoader().loadTestsFromModule(test_singleton_metaclass)
    suite_vector = unittest.TestLoader().loadTestsFromModule(test_vector_class)
    all_tests = unittest.TestSuite([suite_cached, suite_sort, suite_json, suite_singleton, suite_vector])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
    pass