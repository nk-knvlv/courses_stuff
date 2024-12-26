from functools import reduce


def unit_and_sort_lists(lists):
    if len(lists) > 1:
        total_list = reduce(lambda x, y: x + y, lists, [])
    else:
        total_list = lists[0]
    return sorted(total_list)


def factorial(num):
    if num < 0:
        return False
    if num == 0:
        return 0
    result = 1
    for el in range(1, num + 1):
        result *= el
    return result


def is_multiple_of_1000(num):
    if num in range(-999, 999):
        return None
    if num % 1000 == 0:
        return 'millennium'


def get_user_input():
    return input('enter some shit: \n')


def get_venue_by_guest_count(guests_count):
    match guests_count:
        case guests_count if guests_count > 50:
            return 'restaurant'
        case guests_count if guests_count in range(20, 51):
            return 'cafe'
        case guests_count if guests_count in range(1, 20):
            return 'home'
        case _:
            return None


def multiply_by_neg2(num_list):
    return [x * -2 for x in num_list]


def get_even_num_count(num_list):
    return len([x for x in num_list if x % 2 == 0])


def add_dict_key_len_into_key(currencies):
    return {
        x + str(len(x)): y for x, y in currencies.items()
    }


def num_list_shift(num_list):
    if len(num_list) < 2:
        return num_list
    return num_list[1:] + [num_list[0]]


def get_fibonacci_sequence(req_count):
    fib_seq = [0, 1, 1]
    if req_count <= 0:
        return []
    if req_count < 3:
        return fib_seq[0:req_count]
    seq_len = len(fib_seq)
    while seq_len < req_count:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
        seq_len += 1
    return fib_seq
