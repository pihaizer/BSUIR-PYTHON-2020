import os
import argparse
from collections import Counter
import random
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', type=int, metavar='',
                    required=True, help='number of task')
parser.add_argument('-d', '--directory', type=str, help='directory of file')
parser.add_argument('-n', '--number', type=int, help='number of digits')
args = parser.parse_args()


def get_words():

    with open(args.directory, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(
        ".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  
        L = arr[:mid]  
        R = arr[mid:]  

        merge_sort(L)  
        merge_sort(R)  

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


def counting():
    words = get_words()
    words_dict = get_words_dict(words)
    print("amount of words: %d" % len(get_words()))
    print("unique words: %d" % len(words_dict))
    print("all used words:")
    for word in words_dict:
        print(word.ljust(20), words_dict[word])


def sentence():
    cnt = Counter(get_words())
    print(cnt.most_common(args.number))


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
         return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def quick_task():
    str = input("input ur string:\n")
    nums = list(map(int,str.split()))
    quick_sort(nums,0,len(nums)-1)
    print(nums)


def slicing():
    str = input("input ur string:\n")
    nums = str.split()
    print(merge_sort(nums))


def fibonacci_gen(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


def fibonacci():
    print(list(fibonacci_gen(int(input("how many fibonacci numbers wanna see?\n")))))


def main():
    if args.task == 1:
        counting()
    elif args.task == 2:
        sentence()
    elif args.task == 3:
        quick_task()
    elif args.task == 4:
        fibonacci()
    elif args.task == 5:
        slicing()
    else:
        print('wrong input')


if __name__ == "__main__":
    main()
