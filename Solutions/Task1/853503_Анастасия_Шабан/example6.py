

def fibonacci(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        fib_sum = f1 + f2
        f1 = f2
        f2 = fib_sum
        yield f1


def fibonacci_generator(n):
    for fib in fibonacci(n):
        print(fib, end=" ")