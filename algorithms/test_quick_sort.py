import pytest
from basic_algorithms import (
    binary_search,
    bubble_sort,
    dumb_sort,
    shake_sort,
    even_odd_sort,
    comb_sort,
    insertion_sort,
    selection_sort
)
from quick_sort import quick_sort_1, quick_sort_2


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2], [2, 3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([2, 1], [1, 2]),  # Массив в обратном порядке
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_quick_sort_1(input_array, expected_output):
    assert quick_sort_1(0, len(input_array) - 1, input_array) == expected_output


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2], [2, 3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([2, 1], [1, 2]),  # Массив в обратном порядке
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_quick_sort_2(input_array, expected_output):
    assert quick_sort_2(input_array) == expected_output
