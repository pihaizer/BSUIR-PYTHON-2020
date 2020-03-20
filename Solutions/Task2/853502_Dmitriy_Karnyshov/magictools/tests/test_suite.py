import unittest
from . import test_cached_decorator
from . import test_external_sorting
from . import test_json_converter
from . import test_singleton_metaclass
from . import test_vector_class

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_cached_decorator.TestCachedDecorator())
    suite.addTest(test_external_sorting.TestExternalSortingPerfomance())
    suite.addTest(test_external_sorting.TestExternalSortingResult())
    suite.addTest(test_external_sorting.TestExternalSortingErrorOccurences())
    suite.addTest(test_json_converter.TestJsonConverter())
    suite.addTest(test_singleton_metaclass.TestSingletonMetaclass())
    suite.addTest(test_vector_class.TestVectorClass())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())