import unittest

def main():
    tests = unittest.defaultTestLoader.discover('.')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)

if __name__ == "__main__":
    main()
