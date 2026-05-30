# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.

import random

try:
    elements = int(input('Введите количество элементов в матрице: '))
except ValueError:
    print('Введите число.')
    exit()


def print_matrix(matrix: list[list[int]]):
    for row in matrix:
        print(row)


def generate_matrix(el: int) -> list[list[int]]:
    return [
        [random.randint(1, 10) for _ in range(el)]
        for _ in range(el)
    ]


def replace_odd_numbers(matrix: list[list[int]]) -> list[list[int]]:
    return [
        [matrix[i][j] if matrix[i][j] % 2 == 0 else 0 for j in range(len(matrix[i]))]
        for i in range(len(matrix))
    ]


matrix = generate_matrix(elements)
print('Исходная матрица:')
print_matrix(matrix)

print('Нечетные заменены на 0:')
print_matrix(replace_odd_numbers(matrix))
