# В матрице элементы второго столбца возвести в квадрат.

import random

try:
    elements = int(input('Введите количество элементов в матрице: '))
except ValueError:
    print('Введите число.')
    exit()

def generate_matrix(el: int) -> list[list[int]]:
    return [
        [random.randint(1, 10) for _ in range(el)]
        for _ in range(el)
    ]

matrix = generate_matrix(elements)

modify_row = lambda r: r[:1] + [r[1] ** 2] + r[2:]

new_matrix = list(map(modify_row, matrix ))

print("Исходная матрица: ")
for i in matrix:
    print(i)

print("Модифицированная матрица: ")
for i in new_matrix:
    print(i)

