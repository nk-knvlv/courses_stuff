import random
from functools import reduce


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
    return max(range(len(matrix)), key=lambda i: sum([matrix[col_i][i] for col_i in range(len(matrix))]))


matrix = generate_matrix(1, 10, 3, 3)
print(matrix)
print(f"get_matrix_max_value - {get_matrix_max_value(matrix)}")
print(f"get_matrix_min_value - {get_matrix_min_value(matrix)}")
print(f"get_matrix_sum - {get_matrix_sum(matrix)}")
print(f"get_max_sum_row_index - {get_max_sum_row_index(matrix)}")
print(f"get_max_sum_column_index - {get_max_sum_column_index(matrix)}")
