def sort(a: list) -> list:
    return quick_sort(a, 0, len(a) - 1)


def quick_sort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)
    return a


def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


if __name__ == '__main__':
    print(sort([15, 2, 3, 15, 3, 4, 11]))