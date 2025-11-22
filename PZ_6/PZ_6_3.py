# Дан список размера N. Обнулить все его локальные максимумы
# (то есть числа, большие своих соседей).


import random
# Исходный список
try:
    T = int(input("Введите длину списка: "))
    A = [random.randint(0, 100) for i in range(T)]
    N = len(A)

    print("Исходный список:", A)

# Проходим по элементам, кроме первого и последнего (у них только один сосед)
    for i in range(1, N-1):
        if A[i]>A[i-1]:
            if A[i]>A[i+1]:
                A[i] = 0

    print("Результат:      ", A)

except ValueError or NameError as e:
    print(e)
