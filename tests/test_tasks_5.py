from src.tasks_5 import (
    get_harmonic_series_sum,
    replace_odd_by_max,
    get_increase_intervals_count,
    set_max_value_into_main_matrix_diagonal,
    reverse_sentence_words
)
import pytest
from decimal import Decimal, getcontext
from random import randint


@pytest.mark.parametrize(
    "num, exp_res", (
            [1, Decimal(1.0)],
            [2, Decimal(1.5)],
            [3, Decimal('1.833333')],
            [10, Decimal('2.928968')],
            [100, Decimal('5.187377')],
            [0, False],
            [-5, False]
    )
)
def test_get_harmonic_series(num, exp_res):
    assert get_harmonic_series_sum(num) == exp_res


@pytest.mark.parametrize(
    "num_list, exp_res", (
            [[], False],
            [
                [53, 69, 92, 66, 46, 91, 47, 9, 28, 47, 44, 22, 97, 61, 12, 90, 22, 74, 97],
                [53, 69, 97, 97, 97, 91, 47, 9, 97, 47, 97, 97, 97, 61, 97, 97, 97, 97, 97]
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            [
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ],
    )
)
def test_replace_odd_by_max(num_list, exp_res):
    assert replace_odd_by_max(num_list) == exp_res


@pytest.mark.parametrize(
    "num_list, exp_res", (
            [[], 0],
            [
                [53, 69, 92, 66, 46, 91, 47, 9, 28, 47, 44, 22, 97, 61, 12, 90, 22, 74, 97],
                6
            ],
            [
                [1, 2, 3],
                1
            ],
            [
                [1, 2, 3, 2, 4, 1, 0, 10],
                3
            ],
    )
)
def test_get_increase_intervals_count(num_list, exp_res):
    assert get_increase_intervals_count(num_list) == exp_res


@pytest.mark.parametrize(
    "matrix, exp_res", (
            [
                [[7, 6, 0],
                 [6, 6, 8],
                 [9, 2, 9]],
                [[7, 6, 0],
                 [6, 8, 6],
                 [9, 2, 9]]
            ],
            [
                [[5, 9, 4],
                 [2, 7, 2],
                 [0, 8, 4]],
                [[9, 5, 4],
                 [2, 7, 2],
                 [0, 4, 8]]
            ],
            [
                [[9, 4, 5],
                 [2, 9, 7],
                 [8, 0, 9]],
                [[9, 4, 5],
                 [2, 9, 7],
                 [8, 0, 9]],

            ],
            [
                [[0, 4, 5],
                 [9, 8, 9],
                 [5, 7, 0]],
                [[5, 4, 0],
                 [8, 9, 9],
                 [5, 0, 7]]
            ],
            [
                [[4, 5, 3],
                 [1, 7, 9],
                 [6, 7, 8]],
                [[5, 4, 3],
                 [1, 9, 7],
                 [6, 7, 8]]
            ],
            [
                [[5, 5, 4],
                 [5, 3, 8],
                 [9, 8, 5]],
                [[5, 5, 4],
                 [5, 8, 3],
                 [5, 8, 9]]
            ]
    )
)
def test_set_max_value_into_main_matrix_diagonal(matrix, exp_res):
    assert set_max_value_into_main_matrix_diagonal(matrix) == exp_res


@pytest.mark.parametrize(
    "sentence, exp_res", (
            ["Привет мир", "мир Привет"],
            ["Как дела", "дела Как"],
            ["Python - мощный язык", "язык мощный - Python"],
            ["Солнце светит", "светит Солнце"],
            ["Я люблю программировать", "программировать люблю Я"],
            ["Кошки лучше собак", "собак лучше Кошки"]

    )
)
def test_reverse_sentence_words(sentence, exp_res):
    assert reverse_sentence_words(sentence) == exp_res
