def create_fibonacci_generator(count: int = 10):
    a = 1
    yield a
    b = 1
    yield b
    for i in range(count - 2):
        a, b = a+b, a
        yield a


def main():
    fibonacci_generator = create_fibonacci_generator(30)
    for number in fibonacci_generator:
        print(number, end=' ')


if __name__ == "__main__":
    main()