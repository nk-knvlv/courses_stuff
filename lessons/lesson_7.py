from functools import reduce

name_list = {
    'Alex': '1',
    'Vova': '2',
    'Vasya': '3',
    'John': '4',
    'Igor': '5',
    'Nikita': '6',
}
new_list = {}
for name, value in name_list.items():
    new_list[f"{name}_{value}"] = value

new_list = {f"{name}_{value}": value
            for name, value in name_list.items()}

new_list = dict(map(lambda el: (f"{el[0]}_{el[1]}", el[1]), name_list.items()))

# print(new_list)

num = 1231241848128481


# возвращает сумму цифр в числе 1 способ
def get_digit_sum(number: int) -> int:
    return sum([int(str_dig) for str_dig in str(number)])


# возвращает сумму цифр в числе 2 способ

def get_digit_sum_reduce(number: int) -> int:
    return reduce(lambda x, a: x + int(a), [int(i) for i in str(number)])


# находит первое число встречающееся 3 раза подряд

def get_third_entered_element(number: int) -> int:
    elements_count = {}
    number_generator = (x for x in enumerate(str(number)))
    for pair in number_generator:
        i = pair[0]
        el = pair[1]
        if el not in elements_count:
            elements_count[el] = 0
        elements_count[el] += 1
        if elements_count[el] == 3:
            return int(el)
    return 0


