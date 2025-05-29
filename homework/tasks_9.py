from functools import reduce

# 1.	Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.

str_list = ['asfgasdags', 'bbbbbbb', 'cccccc', 'ddddddd']

mod_str_list = [f'{i} - {string}' for i, string in enumerate(str_list)]

# 2. Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

double_key = lambda *args, **kwargs: {key * 2: value for key, value in kwargs.items()}


# 3. Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка.

def even_face_control(func):
    def wrapper(*args, **kwargs):
        numbers = args[0]
        faced_numbers = [num for num in numbers if not num & 1 == 0]  # (҂◡̀_◡́)ᕤ
        new_args = [faced_numbers, *args[1::]]
        return func(*new_args, **kwargs)

    return wrapper


@even_face_control
def num_multiplier(numbers: list[int]) -> int:
    result = reduce(lambda acc, el: acc * el, numbers, 1)
    return result


# 4. Создать универсальный декоратор,
# который меняет порядок аргументов в функции на противоположный.


def arg_reverse(func):
    def wrapper(*args, **kwargs):
        if args:
            args = args[::-1]
        if kwargs:
            kwargs = kwargs[::-1]
        return func(*args, **kwargs)

    return wrapper


@arg_reverse
def foo(numbers: list[int], string: str) -> bool:
    print(numbers, string)
    return True
