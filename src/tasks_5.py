from functools import reduce
from decimal import Decimal, ROUND_FLOOR


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


lst = [1, 2, 3, 2, 4, 1, 0, 10]
result = get_increase_intervals_count(lst)
