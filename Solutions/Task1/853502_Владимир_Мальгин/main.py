import random
import textwrap
import time
import sys
import argparse

import sorts
import fibonacci_generator
import random_numbers_generator
from text_analyser import count_words_sorted, generate_random_sentence


def merge_sort(input_file_name: str, output_file_name: str = None):
    numbers = get_numbers_from_file(input_file_name)
    sorted_numbers = sorts.merge_sort(numbers)
    print_numbers_to_file(sorted_numbers, output_file_name)


def quick_sort(input_file_name: str, output_file_name: str = None):
    numbers = get_numbers_from_file(input_file_name)
    sorted_numbers = sorts.quick_sort(numbers)
    print_numbers_to_file(sorted_numbers, output_file_name)


def words_count(input_file_name: str) -> dict:
    text = get_text_from_file(input_file_name)
    words_dict = count_words_sorted(text)
    for key, value in words_dict.items():
        print(key, ": ", value)
    return words_dict


def generate_sentence(words_dict: dict, size: int):
    words = list(words_dict.keys())[:min(size, len(words_dict))]
    print(generate_random_sentence(words))


def get_numbers_from_file(file_name: str) -> list:
    data = get_text_from_file(file_name)
    numbers = [int(number.strip()) for number in data.split(' ') if number != '']
    return numbers


def get_text_from_file(file_name: str) -> str:
    with open(file_name) as input_file:
        data = input_file.read()
        return data


def print_numbers_to_file(numbers: list, file_name: str):
    if file_name is None:
        for number in numbers:
            print(number, end=' ')
        return
    try:
        with open(file_name, "w") as file:
            for number in numbers:
                file.write(str(number) + ' ')
    except IOError:
        for number in numbers:
            print(number, end=' ')


def print_fibonacci(count: int):
    generator = fibonacci_generator.create_fibonacci_generator(count)
    for number in generator:
        print(number, end=' ')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-nf", "--numbers_file", type=str, help="Input file containing numbers.")
    parser.add_argument("-tf", "--text_file", type=str, help="Input file containing text.")
    parser.add_argument("-of", "--output_file", type=str, help="Output file for some operations.")
    parser.add_argument("-ms", "--merge_sort", action="store_true",
                        help=textwrap.dedent("""\
                        Sorts numbers given in numbers file using merge sort.
                        Prints output to output file if it exists and is valid,
                        to console otherwise.
                        WARNING: Won't work if 'generate numbers' is on."""))
    parser.add_argument("-qs", "--quick_sort", action="store_true",
                        help=textwrap.dedent("""\
                        The same as merge sort, but using quick sort.                        
                        WARNING: Won't work if 'generate numbers' is on."""))
    parser.add_argument("-wc", "--words_count", action="store_true",
                        help="Counts words in a given text file and prints output to console.")
    parser.add_argument("-gs", "--generate_sentence", type=int,
                        help=textwrap.dedent("""\
                        Generates a sentence of {number} words, using the most popular
                        words from 'words count' result. 
                        WARNING: Won't work without 'words_count'."""))
    parser.add_argument("-pf", "--print_fibonacci", type=int,
                        help="Prints {number} fibonacci numbers to console.")
    parser.add_argument("-gn", "--generate_numbers", type=int,
                        help=textwrap.dedent("""\
                        Generates {number} amount of random numbers and
                        saves them to the given output file."""))

    args = parser.parse_args(sys.argv[1:])
    return args


def do_operations(args: argparse.Namespace):
    numbers_file_name = args.numbers_file
    text_file_name = args.text_file
    output_file_name = args.output_file

    if args.generate_numbers:
        random_numbers_generator.generate_random_numbers(count=args.generate_numbers, file_name=output_file_name)
    if args.merge_sort and not args.generate_numbers:
        merge_sort(numbers_file_name, output_file_name)
    elif args.quick_sort and not args.generate_numbers:
        quick_sort(numbers_file_name, output_file_name)
    if args.words_count:
        words_dict = words_count(text_file_name)
        if args.generate_sentence:
            generate_sentence(words_dict, args.generate_sentence)
    if args.print_fibonacci:
        print_fibonacci(args.print_fibonacci)


def main():
    args = parse_args()
    do_operations(args)


if __name__ == '__main__':
    main()
