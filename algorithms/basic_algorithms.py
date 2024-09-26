def linear_search(numbers_list: list[int], target_num: int) -> int:
    for index, num in enumerate(numbers_list):
        if num is target_num:
            return index
    return -1


def binary_search(numbers_list, target_num):
    if not numbers_list:
        return -1
    if len(numbers_list) == 1:
        if numbers_list[0] == target_num:
            return 0
        else:
            return -1
    low = 0
    high = len(numbers_list) - 1
    while low <= high:
        mid = (low + high) // 2

        if numbers_list[mid] == target_num:
            return mid
        if numbers_list[mid] > target_num:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def bubble_sort(num_list):
    is_swap = True
    while is_swap:
        is_swap = False
        for i, el in enumerate(num_list[:-1]):
            if num_list[i] > num_list[i + 1]:
                smaller_value = num_list[i + 1]
                num_list[i + 1] = num_list[i]
                num_list[i] = smaller_value
                is_swap = True
    return num_list


def dumb_sort(num_list: list) -> list:
    is_swap = True
    while is_swap:
        is_swap = False
        for i, el in enumerate(num_list[:-1]):
            if num_list[i] > num_list[i + 1]:
                smaller_value = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = smaller_value
                is_swap = True
            continue
    return num_list


def shake_sort(num_list: list) -> list:
    is_swap = True
    while True:
        for i, el in enumerate(num_list[:-1]):
            if num_list[i] > num_list[i + 1]:
                smaller_value = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = smaller_value
                break
        for i, el in enumerate(num_list[:-1:-1]):
            if num_list[i] > num_list[i + 1]:
                smaller_value = num_list[i]
                num_list[i] = num_list[i + 1]
                num_list[i + 1] = smaller_value
                is_swap = True
        return num_list
