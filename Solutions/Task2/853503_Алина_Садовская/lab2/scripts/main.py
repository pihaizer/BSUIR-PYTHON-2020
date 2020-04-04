import unittest
import sys
from time import sleep
from lab2.tests import *


menu = '\n'.join(['\n', '1) Test Sort', '2) Test JSON', '3) Test Vector', "4) Test Cached", "5) Test Singleton", "or enter 'EXIT'"])

tests_menu = {
    '1': (TestSort, ),
    '2': (TestJsonDump, TestJsonLoad,),
    '3': (TestVector,),
    '4': (TestCached,),
    '5': (TestSingleton,),
}

if __name__ == '__main__':
    while True:
        sleep(.01)
        print(menu)
        user_input = input('Enter test number: ')
        if user_input.lower() == 'exit':
            sys.exit(0)

        if user_input in tests_menu:
            tests = tests_menu[user_input]
            for test in tests:
                suite = unittest.defaultTestLoader.loadTestsFromTestCase(test)
                unittest.TextTestRunner().run(suite)
        else:
            print('Try again!')