import tempfile
import os

RUN_FILE_NAME = 'run_{}.txt'
TEMP_DIR = tempfile.gettempdir()


def create_initial_runs(input_file, run_size):
    """Create the initial runs and divide them evenly among output files.
    Return number of saved runs."""

    run, idx = [], 0
    for number in get_numbers(input_file):
        run.append(number)
        if len(run) == run_size:
            run.sort()
            write_run(run, idx)
            run.clear()
            idx += 1
    # the last run's length may be less than run_size
    if run:
        run.sort()
        write_run(run, idx)
        idx += 1
    return idx


def get_numbers(filename):
    """Generator for numbers in a file."""

    with open(filename, 'r') as f:
        symbol = f.read(1)
        number = ''
        is_escape = lambda ch: ch == ' ' or ch == '\n'
        while symbol:
            if is_escape(symbol):
                while is_escape(symbol):
                    symbol = f.read(1)
                number = validate_input(number)
                yield number
                number = ''
            else:
                number += symbol
                symbol = f.read(1)
        if number:
            yield validate_input(number)


def validate_input(number):
    if not (number.isdigit() or
            ((number.startswith('-') or number.startswith('+')) and number[1:].isdigit())):
        raise ValueError(f"Input file must contain integer numbers. Invalid literal: '{number}'")
    return int(number)


def write_run(run, idx):
    """Write the run to a temp file with given index."""

    run_path = os.path.join(TEMP_DIR, RUN_FILE_NAME.format(idx))
    save_to_file(run, run_path)


def save_to_file(run, filename):
    """Write the run to a given file"""

    with open(filename, 'w') as f:
        for number in run:
            f.writelines(f'{number}\n')


def get_min(array):
    """Get the minimum value and its index."""

    min_val, min_idx = float('inf'), None
    for idx, val in enumerate(array):
        if val < min_val:
            min_val, min_idx = val, idx
    return min_val, min_idx


def join_runs(first_idx, last_idx, run_size):
    """Join runs into bigger ones and return their indices."""

    idx = last_idx
    for i in range(first_idx, last_idx, run_size):
        if i + run_size <= last_idx:
            merge_runs(os.path.join(TEMP_DIR, RUN_FILE_NAME.format(idx)), i, i + run_size)
        else:
            merge_runs(os.path.join(TEMP_DIR, RUN_FILE_NAME.format(idx)), i, last_idx)
        idx += 1
    return last_idx, idx


def merge_runs(output_file, first_index, last_index):
    """Merge runs into one and save to a file with given name."""

    number_generators = [get_numbers(os.path.join(TEMP_DIR, RUN_FILE_NAME.format(idx)))
                         for idx in range(first_index, last_index)]
    numbers = [next(generator) for generator in number_generators]
    general_run = []
    while True:
        min_val, min_idx = get_min(numbers)
        if min_idx is None:
            break
        general_run.append(min_val)
        try:
            numbers[min_idx] = next(number_generators[min_idx])
        except StopIteration:
            numbers[min_idx] = float('inf')
    save_to_file(general_run, output_file)


def sort(input_file, run_size, output_file=None):
    """External sort of a file with integer numbers separated by spaces or '\n'."""

    if run_size <= 1:
        raise ValueError('The size of each partition should be greater than one.')

    output_file = output_file or input_file
    first_idx, last_idx = 0, create_initial_runs(input_file, run_size)
    while last_idx - first_idx > run_size:
        first_idx, last_idx = join_runs(first_idx, last_idx, run_size)
    merge_runs(output_file, first_idx, last_idx)
