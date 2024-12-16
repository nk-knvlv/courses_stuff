import random


def partition(l, r, num_list):
    pivot = random.randint(l, r)
    m = l
    for i, el in enumerate(num_list):
        if el < pivot:
            num_list[i], num_list[m] = num_list[m], num_list[i]
            m += 1
    return m


def fast_sort(l: int, r: int, num_list: list[int]) -> list[int]:
    if (r - l) == 1:
        return num_list
    m = partition(l=l, r=r, num_list=num_list)
    fast_sort(l, m, num_list)
    fast_sort(m, r, num_list)
    return num_list
