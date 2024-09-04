import random
from functools import reduce
from decimal import Decimal, ROUND_FLOOR
from random import randint
from math import sqrt
import pprint
import datetime


def do_operation():
    print('=============== Operator ==============\n'
          'syntax: enter x, y and required operation (+,-,*,/), "stop" for break\n'
          'ex: 8,3,+  .....   #output 11\n')
    while True:
        user_input = input('=> ')
        if user_input == '0':
            break
        input_parts = user_input.split(',')
        if len(input_parts) != 3:
            print('Wrong syntax...')
            continue

        x = int(input_parts[0])
        y = int(input_parts[1])
        operand = input_parts[2]

        if not isinstance(x, int):
            print('Wrong x...')
            continue
        if not isinstance(y, int):
            print('Wrong y...')
            continue
        if operand not in '+,-,*,/':
            print('Wrong operand...')
            continue
        match operand:
            case '+':
                print(x + y)
            case '-':
                print(x - y)
            case '*':
                print(x * y)
            case '/':
                if y == 0:
                    print('zero division error')
                    continue
                print(x / y)


def sum_and_product(x, y):
    return f'sum = {x + y}, product = {x * y}'


def get_denominators_without_num(num):
    return [x for x in range(1, num) if num % x == 0]


def get_friendly_nums_in_interval(start, end):
    friendly_nums = []
    for num in range(start, end + 1):
        num_denominators = get_denominators_without_num(num)
        possible_friendly_num = sum(num_denominators)
        if possible_friendly_num in range(start, end // 2 + 1):
            pos_friend_denominators = get_denominators_without_num(possible_friendly_num)
            if sum(pos_friend_denominators) == num:
                friendly_nums.append([num])
    return friendly_nums


# 4) Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]

def get_harmonic_series_sum(n):
    if n <= 0:
        return False
    if n == 1:
        return Decimal(1)
    harmonic_sum = reduce(lambda x, a: x + (Decimal(1) / Decimal(a)), range(1, n + 1))
    return harmonic_sum.quantize(Decimal('0.000001'), ROUND_FLOOR)


"""
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего
"""


def replace_odd_by_max(num_list: list):
    if len(num_list) != 19:
        return False
    max_value = max(num_list)
    return [max_value if el % 2 == 0 else el for el in num_list]


def get_increase_intervals_count(num_list):
    if len(num_list) < 2:
        return 0
    inc_intervals_count = 0
    is_increase = False
    for i in range(1, len(num_list)):
        if num_list[i] > num_list[i - 1]:
            if not is_increase:
                is_increase = True
                inc_intervals_count += 1
        else:
            is_increase = False
    return inc_intervals_count


"""
Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали.
"""


def generate_test_matrix():
    return [
        [
            randint(0, 10) for _ in range(0, 3)
        ] for x in range(0, 3)
    ]


def set_max_value_into_main_matrix_diagonal(matrix):
    for str_index in range(len(matrix)):
        max_value_index, max_value = max(enumerate(matrix[str_index]), key=lambda x: x[1])
        temp_main_diagonal_el = matrix[str_index][str_index]
        matrix[str_index][str_index] = max_value
        matrix[str_index][max_value_index] = temp_main_diagonal_el
    return matrix

"""
В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы.
"""
def reverse_sentence_words(sentence):
    return ' '.join(sentence.split(' ')[::-1])

"""
Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
"""
def get_interval_dividers(x, y):
    dividers_dict = {}
    for el in range(x, y + 1):
        dividers_dict[el] = []
        for divider in range(2, int(sqrt(el)) + 1):
            if el % divider == 0:
                dividers_dict[el].append(divider)
                if divider != el // divider:  # Добавляем сопряженный делитель
                    dividers_dict[el].append(el // divider)
    return dividers_dict


def get_interval():
    interval = list(map(int, input('press x y').strip().split(' ')))
    if len(interval) != 2 or interval[0] >= interval[1]:
        raise ValueError
    return interval


def run_interval_dividers_script():
    intervals = get_interval()
    pprint.pprint(get_interval_dividers(*intervals))


cities_us = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose",
    "Austin",
    "Jacksonville",
    "Fort Worth",
    "Columbus",
    "San Francisco",
    "Charlotte",
    "Indianapolis",
    "Seattle",
    "Denver",
    "Washington, D.C.",
    "Boston"
]

"""
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут.
"""
def generate_train_schedule(train_count):
    trains_schedule = {}
    now = datetime.datetime.now()
    for _ in range(0, train_count):
        arrival_time = datetime.datetime.combine(now.date(), datetime.time(randint(0, 23), randint(0, 59)))
        departure_time = arrival_time + datetime.timedelta(hours=randint(1, 23), minutes=randint(1, 59))
        trains_schedule[randint(1000, 9999)] = {
            'arrival': {
                'location': random.choice(cities_us),
                'time': arrival_time},
            'departure': {
                'location': random.choice(cities_us),
                'time': departure_time
            }
        }
    return trains_schedule


def get_long_way_trips(trains_schedule):
    return {
        train_num for train_num in trains_schedule if
        (trains_schedule[train_num]['departure']['time'] - trains_schedule[train_num]['arrival'][
            'time']) > datetime.timedelta(hours=7, minutes=20)
    }


schedule = generate_train_schedule(10)

pprint.pprint(schedule)

long_trips = get_long_way_trips(schedule)

pprint.pprint(long_trips)
