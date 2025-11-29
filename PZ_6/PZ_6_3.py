# Дан список размера N. Обнулить все его локальные максимумы
# (то есть числа, большие своих соседей).


import random


def replace_maximum(spisok: list[int]) -> list[int]:
    return_list = spisok.copy()
    for i in range(1, len(spisok) - 1):
        if spisok[i-1] < spisok[i] > spisok[i+1]:
            return_list[i] = 0
    if spisok[0] > spisok[1]:
        return_list[0] = 0
    if spisok[-1] > spisok[-2]:
        spisok[-1] = 0
    return return_list


try:
    n = int(input('Введите размер списка: '))
except ValueError:
    print('Введите число')
    exit()

nums = [random.randint(0, 100) for i in range(n)]

print(nums)
print(replace_maximum(nums))
