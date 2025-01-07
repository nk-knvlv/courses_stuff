# 1. inches to centimeters (дюймы - ширина большого пальца)
def convert_inches_to_centimeters(value: int):
    return value * 2.54


# 2. Centimeters to inches
def convert_centimeters_to_inches(value: int):
    if value == 0:
        return value
    return value / 2.54


# 3. Miles to kilometers (мили с древнего рима 1482 м)
def convert_miles_to_kilometers(value: int):
    return value * 1.482


# 4. Kilometers to miles
def convert_kilometers_to_miles(value: int):
    if value == 0:
        return value
    return value / 1.482


# 5. Pounds to Kilograms
def convert_pounds_to_kilograms(value: int):
    return value * 16.3805


# 6. Kilograms to Pounds
def convert_kilograms_to_pounds(value: int):
    if value == 0:
        return value
    return value / 16.3805


# 7. Ounces to grams
def convert_ounces_to_grams(value: int):
    return value * 28.35


# 8. Grams to Ounces
def convert_grams_to_ounces(value: int):
    if value == 0:
        return value
    return value / 28.35


# 9. Gallons to Liters
def convert_gallons_to_liters(value: int):
    return value * 4.5


# 10. Liters to Gallons
def convert_liters_to_gallons(value: int):
    if value == 0:
        return value
    return value / 4.5


# 11. Pints to Liters
def convert_pints_to_liters(value: int):
    return value * 0.473


# 12. Liters to pints
def convert_liters_to_pints(value: int):
    if value == 0:
        return value
    return value / 0.473
