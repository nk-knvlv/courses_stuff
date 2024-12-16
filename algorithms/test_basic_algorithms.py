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


@pytest.mark.parametrize("arr, target, expected", [
    ([], 3, -1),  # Пустой массив
    ([5], 3, -1),  # Один элемент (отсутствие)
    ([5], 5, 0),  # Один элемент (присутствие)
    ([1, 3, 5, 7, 9, 11], 9, 4),  # Массив (присутствие)
    ([1, 3, 5, 7, 9, 11], 4, -1),  # Массив (отсутствие)
])
def test_binary_search(arr, target, expected):
    assert binary_search(arr, target) == expected


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_bubble_sort(input_array, expected_output):
    assert bubble_sort(input_array) == expected_output


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_dumb_sort(input_array, expected_output):
    assert dumb_sort(input_array) == expected_output


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([2, 1], [1, 2]),  # Массив в обратном порядке
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_shake_sort(input_array, expected_output):
    assert shake_sort(input_array) == expected_output


@pytest.mark.parametrize("input_array, expected_output", [
    ([], []),  # Пустой массив
    ([1], [1]),  # Массив с одним элементом
    ([5, 4, 3], [3, 4, 5]),  # Отсортированный массив
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Массив в обратном порядке
    ([2, 1], [1, 2]),  # Массив в обратном порядке
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Отсортированный массив
    ([3, 1, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])  # Массив с дубликатами
])
def test_even_odd_sort(input_array, expected_output):
    assert even_odd_sort(input_array) == expected_output


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
def test_comb_sort(input_array, expected_output):
    assert comb_sort(input_array) == expected_output


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
def test_insertion_sort(input_array, expected_output):
    assert insertion_sort(input_array) == expected_output


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
def test_selection_sort(input_array, expected_output):
    assert selection_sort(input_array) == expected_output


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
def test_selection_sort(input_array, expected_output):
    assert selection_sort(input_array) == expected_output
