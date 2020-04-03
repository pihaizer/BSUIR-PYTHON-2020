import sys
import argparse
import random

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[0:])
    print(sys.argv[1:])
    if namespace.number_func == 1:
        word_count()
        print(word_count())
    elif namespace.number_func == 2:
        quick_sort(namespace.argument)
    elif namespace.number_func == 3:
        merge_sort(namespace.argument)
    elif namespace.number_func == 4:
        fibonacci_generator(int(namespace.argument))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_func', choices=[1, 2, 3, 4], type=int, default=4)
    parser.add_argument('argument', default=10)
    return parser


def word_count():
    di = {}
    with open("text.txt", "r") as file:
        text_string = file.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

    for word in match_pattern:
        count = di.get(word, 0)
        di[word] = count + 1

    di_list = di.keys()

    for words in di_list:
        print(words, di[words])

    print("////////////////////////////////////////////////////////")

    list_d = list(di.items())
    list_d.sort(key=lambda i: i[1], reverse=True)

    for i in list_d:
        print(i[0], ':', i[1])

    print("////////////////////////////////////////////////////////")

    s = "-".join(i[0] for i in list_d[0:10])
    print(s)


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        quick_sort(array, begin, pivot - 1)
        quick_sort(array, pivot + 1, end)

    return quick_sort(array, begin, end)


with open("number.txt", "r") as file:
    L = list(map(int, file.read().split(" ")))

quick_sort(L)
print("Быстрая сортировка")
print(L)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_length, right_length = len(left_list), len(right_list)

    for _ in range(left_length + right_length):
        if left_list_index < left_length and right_list_index < right_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


with open("number.txt", "r") as file:
    S = list(map(int, file.read().split(" ")))
print("Сортировка слиянием")
S = merge_sort(S)
print(S)


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


if __name__ == '__main__':
    main()