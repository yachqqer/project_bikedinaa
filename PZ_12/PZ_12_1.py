# В матрице элементы второго столбца возвести в квадрат.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

modify_row = lambda r: r[:1] + [r[1] ** 2] + r[2:]

new_matrix = list(map(modify_row, matrix))

print("Новая матрица:")
print(new_matrix)

