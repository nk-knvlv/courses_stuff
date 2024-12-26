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


def bubble_sort(num_list: list[int]) -> list[int]:
    is_swap = True
    while is_swap:
        is_swap = False
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                is_swap = True
    return num_list


def dumb_sort(num_list: list[int]) -> list[int]:
    is_swap = True
    while is_swap:
        is_swap = False
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                is_swap = True
            continue
    return num_list


def shake_sort(num_list: list[int]) -> list[int]:
    if len(num_list) < 2:
        return num_list
    low = 0
    high = len(num_list) - 1
    while low < high:
        for i in range(low, high):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        high -= 1
        for i in range(high, low, -1):
            if num_list[i] < num_list[i - 1]:
                num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
        low += 1
    return num_list


def even_odd_sort(num_list: list[int]) -> list[int]:
    if len(num_list) < 2:
        return num_list
    even_odd_switch = 0
    low = 0
    high = len(num_list) - 1
    pure_sort_passing = []
    while len(pure_sort_passing) < 2:
        pure_sort_passing.append(even_odd_switch)
        for i in range(low + even_odd_switch, high, 2):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                if even_odd_switch in pure_sort_passing:
                    pure_sort_passing.remove(even_odd_switch)
        even_odd_switch = 1 - even_odd_switch  # swap even to odd and vice versa.
    return num_list


def comb_sort(num_list: list[int]) -> list[int]:
    if len(num_list) < 2:
        return num_list
    # Общепризнанный оптимальный фактор уменьшения
    reduction_factor = 1.247
    count = len(num_list)
    between_el_dist = count
    is_swap = True
    # если проходы с расстоянием больше 1 закончены, нужна финальная проверка классическим пузырьком
    # которая вызывается условием or between_el_dist > 1
    while is_swap or between_el_dist > 1:
        between_el_dist = max(1, int(between_el_dist // reduction_factor))

        high = count - between_el_dist

        is_swap = False
        for i in range(0, high):
            if num_list[i] > num_list[i + between_el_dist]:
                num_list[i], num_list[i + between_el_dist] = num_list[i + between_el_dist], num_list[i]
                is_swap = True
    return num_list


def insertion_sort(num_list: list[int]) -> list[int]:
    # моржовый оператор := позволяет внутри выражения присвоить переменную для дальнейшего использования
    if (length := len(num_list)) < 2:
        return num_list

    for i in range(1, length):
        for j in range(i, 0, -1):
            if num_list[j - 1] > num_list[j]:
                num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
            else:
                break
    return num_list


def selection_sort(num_list: list[int]) -> list[int]:
    if (length := len(num_list)) < 2:
        return num_list

    for i in range(length):
        current_max_index = 0
        for j in range(length - i):
            if num_list[j] > num_list[current_max_index]:
                current_max_index = j
        # no swap if index don't changed
        if current_max_index != length - i - 1:
            num_list[length - i - 1], num_list[current_max_index] = num_list[current_max_index], num_list[length - i - 1]
    return num_list


a = [5, 4, 3]

print(selection_sort(a))
