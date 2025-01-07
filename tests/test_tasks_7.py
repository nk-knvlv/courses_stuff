from homework.tasks_7 import (
    convert_inches_to_centimeters,
    convert_centimeters_to_inches,
    convert_miles_to_kilometers,
    convert_kilometers_to_miles,
    convert_pounds_to_kilograms,
    convert_kilograms_to_pounds,
    convert_ounces_to_grams,
    convert_grams_to_ounces,
    convert_gallons_to_liters,
    convert_liters_to_gallons,
    convert_pints_to_liters,
    convert_liters_to_pints
)
import pytest
from decimal import Decimal


# Тесты с использованием @pytest.mark.parametrize
@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 2.54),
        (0, 0),
        (-1, -2.54)
    ]
)
def test_convert_inches_to_centimeters(enter_value, expected_value):
    assert convert_inches_to_centimeters(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (2.54, 1),
        (0, 0),
        (-2.54, -1)
    ]
)
def test_convert_centimeters_to_inches(enter_value, expected_value):
    assert convert_centimeters_to_inches(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 1.60934),
        (0, 0),
        (-1, -1.60934)
    ]
)
def test_convert_miles_to_kilometers(enter_value, expected_value):
    assert convert_miles_to_kilometers(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1.60934, 1),
        (0, 0),
        (-1.60934, -1)
    ]
)
def test_convert_kilometers_to_miles(enter_value, expected_value):
    assert convert_kilometers_to_miles(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 0.453592),
        (0, 0),
        (-1, -0.453592)
    ]
)
def test_convert_pounds_to_kilograms(enter_value, expected_value):
    assert convert_pounds_to_kilograms(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (0.453592, 1),
        (0, 0),
        (-0.453592, -1)
    ]
)
def test_convert_kilograms_to_pounds(enter_value, expected_value):
    assert convert_kilograms_to_pounds(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 28.3495),
        (0, 0),
        (-1, -28.3495)
    ]
)
def test_convert_ounces_to_grams(enter_value, expected_value):
    assert convert_ounces_to_grams(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (28.3495, 1),
        (0, 0),
        (-28.3495, -1)
    ]
)
def test_convert_grams_to_ounces(enter_value, expected_value):
    assert convert_grams_to_ounces(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 3.78541),
        (0, 0),
        (-1, -3.78541)
    ]
)
def test_convert_gallons_to_liters(enter_value, expected_value):
    assert convert_gallons_to_liters(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (3.78541, 1),
        (0, 0),
        (-3.78541, -1)
    ]
)
def test_convert_liters_to_gallons(enter_value, expected_value):
    assert convert_liters_to_gallons(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (1, 0.473176),
        (0, 0),
        (-1, -0.473176)
    ]
)
def test_convert_pints_to_liters(enter_value, expected_value):
    assert convert_pints_to_liters(enter_value) == pytest.approx(expected_value)


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        (0.473176, 1),
        (0, 0),
        (-0.473176, -1)
    ]
)
def test_convert_liters_to_pints(enter_value, expected_value):
    assert convert_liters_to_pints(enter_value) == pytest.approx(expected_value)
