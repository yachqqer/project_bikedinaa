# Дано вещественное число - цена 1 кг конфет.
# Вывести стоимость 1.2, 1.4,.. 2кг конфет.

try:
    a = float(input('Введите цену: '))

    for i in range(12, 22, 2):
        w = i / 10
        s = a * w
        print(f" {s} руб. - стоимость за {w} кг конфет")


except ValueError:
    print("Вы ввели не число!")
except  Exception as e:
    print(f"Ошибка: {e}")




