import os
import random
import tempfile
import time
import winsound

from typing import IO
from lab2_merge_sort.exceptions import MergeSortError

MB: int = 1048576
MAX_FILE_BUFFER: int = 128 * MB


def merge_sort(file_name: str, output_file_name=None):
    file = open(file_name, "r+", encoding="ascii")
    file_size = os.path.getsize(file_name)

    sort_or_split(file, file_size, output_file_name)


def sort_or_split(file: IO, file_size, output_file_name=None):
    if file_size < MAX_FILE_BUFFER:
        sort_file(file, output_file_name)
    else:
        split_and_sort(file, file_size, output_file_name)


def sort_file(file, output_file_name=None):
    file.seek(0)
    data = file.read()
    numbers = [float(number_str) for number_str in data.strip().split(' ')]
    numbers = sorted(numbers)
    if output_file_name is not None:
        output_file = open(output_file_name, "w")
    else:
        output_file = file
        output_file.truncate(0)
        output_file.seek(0)
    for number in numbers:
        output_file.write("{} ".format(number))


def split_and_sort(file: IO, file_size, output_file_name=None):
    file.seek(file_size // 2)
    cur_char = file.read(1)
    while cur_char.isdigit() or cur_char in '-.':
        cur_char = file.read(1)
    cur_position = file.tell()
    file.seek(0)
    tmp1 = tempfile.TemporaryFile("w+", encoding="ascii")
    tmp2 = tempfile.TemporaryFile("w+", encoding="ascii")
    tmp1.write(file.read(cur_position))
    tmp2.write(file.read())
    sort_or_split(tmp1, cur_position)
    sort_or_split(tmp2, file_size - cur_position)
    if output_file_name is not None:
        file = open(output_file_name)
    merge_files(tmp1, tmp2, file)


def merge_files(file1, file2, output_file):  # assuming files contain a lot of numbers
    output_file.truncate(0)
    output_file.seek(0)
    file1.seek(0)
    file2.seek(0)
    number1 = read_number(file1)
    number2 = read_number(file2)
    while True:
        if number1 < number2:
            output_file.write(str(number1) + ' ')
            number1 = read_number(file1)
            if number1 is None:
                break
        else:
            output_file.write(str(number2) + ' ')
            number2 = read_number(file2)
            if number2 is None:
                break
    if number1 is None:
        while number2 is not None:
            output_file.write(str(number2) + ' ')
            number2 = read_number(file2)
    elif number2 is None:
        while number1 is not None:
            output_file.write(str(number1) + ' ')
            number1 = read_number(file1)


def read_number(file: IO):
    while True:  # looking for number beginning
        cur_char = file.read(1)
        if not (cur_char.isdigit() or cur_char.isspace() or cur_char in '-'):
            raise MergeSortError("Unexpected symbol: " + cur_char)
        if cur_char.isspace():
            continue
        elif cur_char == '':
            return None
        else:
            break
    number = cur_char
    while not (cur_char.isspace() or cur_char == ''):
        cur_char = file.read(1)
        number += cur_char
    try:
        floated_number = float(number)
    except TypeError:
        raise MergeSortError("Invalid number: " + number)
    return floated_number


if __name__ == '__main__':
    with open('S:/numbers.txt', 'w', encoding="ascii") as f:
        f.writelines('{} '.format(random.randint(-1000000, 1000000)) for _ in range(500000))
    # start_time = time.time()
    # sort('S:/numbers.txt')
    # print(time.time() - start_time)
    # winsound.Beep(800, 1000)
