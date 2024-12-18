import random


def partition(left, right, num_list):
    pivot_index = random.randint(left, right)  # Случайный индекс для опорного элемента
    pivot_value = num_list[pivot_index]  # Значение опорного элемента
    num_list[pivot_index], num_list[right] = num_list[right], num_list[
        pivot_index]  # Перемещение опорного элемента в конец
    store_index = left  # Инициализация индекса для хранения элементов меньше опорного

    for i in range(left, right):
        if num_list[i] < pivot_value:  # Если текущий элемент меньше опорного
            num_list[store_index], num_list[i] = num_list[i], num_list[store_index]  # Меняем местами
            store_index += 1  # Увеличиваем индекс хранения

    # Перемещаем опорный элемент на его финальную позицию
    num_list[store_index], num_list[right] = num_list[right], num_list[store_index]
    return store_index  # Возвращаем индекс опорного элемента


def quick_sort_1(left: int, right: int, num_list: list[int]) -> list[int]:
    if left < right:  # Проверка, что есть более одного элемента
        m = partition(left, right, num_list)  # Разделяем массив и получаем индекс опорного элемента
        quick_sort_1(left, m - 1, num_list)  # Сортируем левую часть
        quick_sort_1(m + 1, right, num_list)  # Сортируем правую часть
    return num_list  # Возвращаем отсортированный массив


def quick_sort_2(num_list: list[int]) -> list[int]:
    if (list_len := len(num_list)) <= 1:
        return num_list

    pivot = num_list[random.randint(0, list_len - 1)]

    left = list(filter(lambda x: x < pivot, num_list))
    center = list(filter(lambda x: x == pivot, num_list))
    right = list(filter(lambda x: x > pivot, num_list))

    return quick_sort_2(left) + center + quick_sort_2(right)


test_list = [2, 1]

quick_sort_1(0, len(test_list) - 1, test_list)
