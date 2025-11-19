# С помощью функции получить вертикальную и горизонтальную линии.
# линия проводится многократной печатью символа.
# Заключить слово в рамку из полученных линий.

try:
    def main (a):
        b = len(a)
        c = "-"*b
        return c

    a = input("Введите слово: ")

    print(f"{main(a) + "-" * 2} ")
    print(f"|{a}|")
    print(f"{main(a) + "-" * 2}")
except ValueError:
    print("Вы ввели не число!")
except  Exception as e:
    print(f"Ошибка: {e}")
