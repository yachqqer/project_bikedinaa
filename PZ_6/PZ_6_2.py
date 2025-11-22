# Дан список А размера N и целые числа К и L (1 < К <L<N). Переставить в обратном
# порядке элементы списка, расположенные между элементами Ак и AL, включая эти
# элементы.


# Библиотека для создания списка
import random

# Создание списка
try:
    N = int(input("Введите число: "))
    A = [random.randint(0, 100) for i in range(N)]
    print(A)
except ValueError:
    print("Вы ввели не число!")
    exit()
try:
    N = int(input("Введите число: "))
except ValueError:
    print("Вы ввели не число!")
    exit()


try:
    K, L = int(input("Введите первое число: ")), int(input("Введите второе число: "))
except ValueError:
    exit()
# Само переворачивание
A[K - 1:L] = A[K - 1:L][::-1]
print("Результат:", A)
