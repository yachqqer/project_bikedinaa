# Дано целое N (>0). Используя операции деления нацело
# и взятие остатка от деления, найти количество и сумму его цифр.

try:
    n = int(input("Введите целое число: "))

    nums_sum = 0
    nums_count = 0
    while n != 0:
        nums_count += 1
        nums_sum += n % 10
        n //= 10
    print("Количество цифр в числе: ", nums_count)
    print("Сумма цифр в числе: ", nums_sum)

except ValueError:
    print("Вы ввели не число!")
except  Exception as e:
    print(f"Ошибка: {e}")




