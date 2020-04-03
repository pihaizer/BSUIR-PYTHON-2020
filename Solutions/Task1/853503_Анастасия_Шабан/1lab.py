from  example1 import word_count
from example3 import quick_sort_func
from example5 import merge_sort_func
from example6 import fibonacci_generator
import sys
import argparse

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    print(namespace)
    if namespace.number_func == 1:
        word_count()
        print(word_count(namespace.argument))
    elif namespace.number_func == 2:
        quick_sort_func(namespace.argument)
    elif namespace.number_func == 3:
        merge_sort_func(namespace.argument)
    elif namespace.number_func == 4:
        fibonacci_generator(int(namespace.argument))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_func', choices=[1, 2, 3, 4], type=int, default=4)
    parser.add_argument('argument', default=10)
    return parser


main()