def sort(a: list) -> list:
    work_array = a.copy()
    return split(a)


def split(a: list) -> list:
    if len(a) < 2:
        return a
    middle = int(len(a) / 2)
    first = a[:middle]
    second = a[middle:]
    return merge(split(first), split(second))


def merge(a: list, b: list) -> list:
    result: list = []
    a_len = len(a)
    b_len = len(b)
    while a_len > 0 and b_len > 0:
        if a[0] < b[0]:
            result.append(a.pop(0))
            a_len -= 1
        else:
            result.append(b.pop(0))
            b_len -= 1
    result.extend(a)
    result.extend(b)
    return result


if __name__ == '__main__':
    print(sort([15, 2, 3, 15, 3, 4, 11]))
