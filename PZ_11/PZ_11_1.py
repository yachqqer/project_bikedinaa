# Из последовательности на n целых чисел создать новую последовательность, в
# которой каждый последующий элемент равен квадрату суммы двух соседних элементов.

import random

try:
    n = int(input("введите число: "))
except ValueError:
    print("напишите число")
    exit()

star = []
for i in range(n):
    star.append(random.randint(1,10))

def quare(num):
    left_neighbors = [0] + list(num[:-1])
    right_neighbors = list(num[1:]) + [0]

    return list(map(lambda x, y: (x + y) ** 2, left_neighbors, right_neighbors))



result = quare(star)

print("Исходная последовательность:", star)
print("Новая последовательность:", result)

