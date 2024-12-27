import random
from functools import reduce
from pprint import pprint


# Создать матрицу случайных чисел от a до b, размерность матрицы n*m
def generate_matrix(a, b, n, m):
    return [
        [random.randint(a, b) for _ in range(n)]
        for _ in range(m)
    ]


# Найти максимальный элемент матрицы.

def get_matrix_max_value(matrix):
    return max([max(row) for row in matrix])


# Найти минимальный элемент матрицы.

def get_matrix_min_value(matrix):
    return min([min(row) for row in matrix])


# Найти сумму всех элементов матрицы.
def get_matrix_sum(matrix):
    return sum(reduce(lambda s, x: s + x, matrix))


# Найти индекс ряда с максимальной суммой элементов.

def get_max_sum_row_index(matrix):
    # джус от gpt (҂◡̀_◡́)ᕤ
    return max(range(len(matrix)), key=lambda i: sum(matrix[i]))


# Найти индекс колонки с максимальной суммой элементов.
def get_max_sum_column_index(matrix):
    # (҂◡̀_◡́)ᕤ
    return max(range(len(matrix[0])), key=lambda i: sum([matrix[col_i][i] for col_i in range(len(matrix))]))


# Найти индекс ряда с минимальной суммой элементов
def get_min_sum_row_index(matrix):
    return min(range(len(matrix)), key=lambda i: sum(matrix[i]))


# Найти индекс колонки с минимальной суммой элементов.
def get_min_sum_column_index(matrix):
    return min(range(len(matrix[0])), key=lambda i: sum([matrix[col_i][i] for col_i in range(len(matrix))]))


# Обнулить все элементы выше главной диагонали.
def reset_above_main_diag(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][:i + 1] + [0 for el_i in range(1, len(matrix[i])) if el_i > i]
    return matrix


# Обнулить все элементы ниже главной диагонали.
def reset_below_main_diag(matrix):
    for i in range(len(matrix)):
        matrix[i] = [0 for _ in range(i)] + matrix[i][i:]
    return matrix


# Создать матрицу равную сумме matrix_a и matrix_b.
def get_matrix_sum(matrix_a, matrix_b):
    return [
        [matrix_a[row_i][i] + matrix_b[row_i][i]
         for i in range(len(matrix_a[row_i]))
         ] for row_i in range(len(matrix_a))
    ]


def get_matrix_difference(matrix_a, matrix_b):
    return [
        [matrix_a[row_i][i] - matrix_b[row_i][i]
         for i in range(len(matrix_a[row_i]))
         ] for row_i in range(len(matrix_a))
    ]

# Создать новую матрицу равную matrix_a умноженной на g. g вводится с
# клавиатура
def multyply_matrix_from_input():
    n = 3
    while (enter_num := int(input('enter num'))) != 'stop':
        matrix = generate_matrix(1, 10, n, n)
        print(matrix)
        print([list(map(lambda x: x * enter_num, row)) for row in matrix])


n = random.randint(3, 6)
m = random.randint(3, 6)
matrix_a = generate_matrix(1, 10, n, n)
matrix_b = generate_matrix(1, 10, n, n)
# print(matrix_a)
# print(matrix_b)
# print(f"get_matrix_max_value - {get_matrix_max_value(matrix)}")
# print(f"get_matrix_min_value - {get_matrix_min_value(matrix)}")
# print(f"get_matrix_sum - {get_matrix_sum(matrix)}")
# print(f"get_max_sum_row_index - {get_max_sum_row_index(matrix)}")
# print(f"get_max_sum_column_index - {get_max_sum_column_index(matrix)}")
# print(f"get_min_sum_row_index - {get_min_sum_row_index(matrix)}")
# print(m)
# pprint(f"reset_above_main_diag - {reset_above_main_diag(matrix)}")
# pprint(f"reset_below_main_diag - {reset_below_main_diag(matrix)}")
# pprint(f"get_matrix_sum - {get_matrix_sum(matrix_a, matrix_b)}")
pprint(f"multyply_matrix_from_input - {multyply_matrix_from_input()}")
