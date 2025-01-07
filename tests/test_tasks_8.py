import math
from homework.tasks_8 import (
    fact2,
    is_palindrome, sin1
)
import pytest


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 1),
        (0, 0),
        (9, 945),
        (6, 48),
    ]
)
def test_fact2(enter_value, expected_value):
    assert fact2(enter_value) == pytest.approx(expected_value)


# Здесь предполагается, что функция Sin1 уже определена

@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        ('sor', False),
        ('', False),
        ('sos', True),
        ('poop', True),
    ]
)
def test_is_palindrome(enter_value, expected_value):
    assert is_palindrome(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "x, epsilon, expected_approx",
    [
        (0, 0.1, 0),  # sin(0) = 0
        (math.pi / 6, 0.01, 0.5),  # sin(π/6) ≈ 0.5
        (math.pi / 4, 0.01, math.sqrt(2) / 2),  # sin(π/4) ≈ √2/2
        (math.pi / 2, 0.01, 1),  # sin(π/2) = 1
        (math.pi, 0.01, 0),  # sin(π) = 0
        (3 * math.pi / 2, 0.01, -1),  # sin(3π/2) = -1
        (2 * math.pi, 0.01, 0),  # sin(2π) = 0
        # Добавьте дополнительные тестовые случаи по вашему выбору
    ]
)
def test_sin1(x, epsilon, expected_approx):
    assert sin1(x, epsilon) == pytest.approx(expected_approx, rel=epsilon)
