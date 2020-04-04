import pytest
import random

from .. import merge_sort


@pytest.fixture
def generate_small_file():
    with open('numbers_small.txt', 'w', encoding="ascii") as f:
        f.writelines('{} '.format(random.random()) for _ in range(50000))
    return 'numbers_small.txt'


def test_small_file(generate_small_file):
    merge_sort(generate_small_file)
