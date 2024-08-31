from src.tasks_5 import (
    get_harmonic_series_sum,
    replace_odd_by_max,
    get_increase_intervals_count
)
import pytest
from decimal import Decimal, getcontext
import random


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
