from src.tasks import (
    factorial,
    unit_and_sort_lists,
    is_multiple_of_1000,
    get_venue_by_guest_count,
    get_user_input,
    multiply_by_neg2,
    get_even_num_count,
    add_dict_key_len_into_key,
    num_list_shift,
    get_fibonacci_sequence
)
import pytest


@pytest.mark.parametrize(
    "n, result",
    [
        (0, 0),
        (1, 1),
        (5, 120),
        (-1, False),

    ]
)
def test_factorial(n, result):
    assert factorial(n) == result


@pytest.mark.parametrize(
    "lists, result", [

        ([[]], []),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1, 3, 5], [2, 4, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 2, 3], [2, 4, 5], [1, 3, 6]], [1, 1, 2, 2, 3, 3, 4, 5, 6]),
        ([[-2, -1, 0], [1, 2, 3]], [-2, -1, 0, 1, 2, 3])
    ]
)
def test_unit_and_sort_lists(lists, result):
    assert unit_and_sort_lists(lists) == result


@pytest.mark.parametrize(
    "num, result", [

        (0, None),
        (1000, 'millennium'),
        (100000000000000, 'millennium'),
        (-20000, 'millennium'),
        (-19999, None)
    ]
)
def test_is_multiple_of_1000(num, result):
    assert is_multiple_of_1000(num) == result


@pytest.mark.parametrize(
    "input_data, result", [
        (60, 'restaurant'),
        (30, 'cafe'),
        (5, 'home'),
        (-20000, None),
        (0, None),
    ]
)
def test_get_venue_by_guest_count(monkeypatch, input_data, result):
    monkeypatch.setattr('builtins.input', lambda _: input_data)
    guest_count = get_user_input()
    assert get_venue_by_guest_count(guest_count) == result


@pytest.mark.parametrize(
    "list_in, result", [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20]),
        ([-3, -5, 2, 13, -100, 1, 0], [6, 10, -4, -26, 200, -2, 0]),
        ([], []),
        ([0], [0]),
        ([1], [-2])
    ]
)
def test_multiply_by_neg2(list_in, result):
    assert multiply_by_neg2(list_in) == result


@pytest.mark.parametrize(
    "num_list, even_num_count", [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([-3, -5, 2, 13, -100, 1, 0], 3),
        ([], 0),
        ([0], 1),
        ([1, 3, 13, 17], 0)
    ]
)
def test_get_even_num_count(num_list, even_num_count):
    assert get_even_num_count(num_list) == even_num_count


@pytest.mark.parametrize("input_dict, expected_output", [
    ({'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'},
     {'test4': 'test_value', 'europe6': 'eur', 'dollar6': 'usd', 'ruble5': 'rub'}),

    ({'key': 'value'}, {'key3': 'value'}),

    ({'empty': '', 'long_key': 'value'}, {'empty5': '', 'long_key8': 'value'}),

    ({'a': 'alpha', 'b': 'beta'}, {'a1': 'alpha', 'b1': 'beta'})
])
def test_add_dict_key_len_into_key(input_dict, expected_output):
    assert add_dict_key_len_into_key(input_dict) == expected_output


# Параметризованные тесты для функции shift_left
@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),  # Простой случай
    ([7, 8, 9], [8, 9, 7]),  # Случай с 3 элементами
    ([10], [10]),  # Случай с одним элементом
    ([], []),  # Случай с пустым списком
    ([1, 2], [2, 1]),  # Случай с двумя элементами
])
def test_num_list_shift(input_list, expected_output):
    assert num_list_shift(input_list) == expected_output


@pytest.mark.parametrize("fib_list_count, expected_output", [
    (1, [0]),  # 1-е число Фибоначчи
    (5, [0, 1, 1, 2, 3]),  # [0, 1, 1, 2, 3] -> [1, 1, 2, 3, 0]
    (8, [0, 1, 1, 2, 3, 5, 8, 13]),  # [0, 1, 1, 2, 3, 5, 8, 13] -> [1, 1, 2, 3, 5, 8, 13, 0]
    (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]),  # [0, 1, ..., 377] -> [1, 1, ..., 0]
    (30, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
          46368, 75025, 121393, 196418, 317811, 514229])  # [0, 1, ..., 832040] -> [1, 1, ..., 0]
])
def test_get_fibonacci_sequence(fib_list_count, expected_output):
    assert get_fibonacci_sequence(fib_list_count) == expected_output
