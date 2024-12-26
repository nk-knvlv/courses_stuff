from random import randint

rand_num_list = [randint(1, 100) for _ in range(0, 10)]


def get_sum_mid_minmax(num_list: list[int]) -> str:
    list_sum = sum(num_list)
    mid = list_sum / len(num_list)
    min_val = min(num_list)
    max_val = max(num_list)
    return f'sum - {list_sum}, mid - {mid}, min - {min_val}, max - {max_val}'


print(rand_num_list)
print(get_sum_mid_minmax(rand_num_list))
