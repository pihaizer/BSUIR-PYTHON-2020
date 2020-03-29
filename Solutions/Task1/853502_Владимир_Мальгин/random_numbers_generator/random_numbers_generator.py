import random


def generate_random_numbers(count: int, file_name="../files/numbers.txt"):
    with(open(file_name, 'w')) as file:
        for i in range(count):
            file.write(str(random.randint(-100000, 100000)) + ' ')


if __name__ == "__main__":
    generate_random_numbers(1000)
