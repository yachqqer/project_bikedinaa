# Описать функцию DigitCountSum(K, C, S), находящую количество С цифр целого положительного числа K,
# а также их сумму S (K -- входной, С и S - выходные параметры целого типа).
# С помощью этой функции найти количество и сумму цифр для каждого из пяти данных целых чисел.

def DigitCountSum(k: str) -> tuple[int, int]:
    nums = [int(i) for i in k]
    return len(nums), sum(nums)


for i in range(5):

    k = input(f'Введите {i+1} число: ')
    if not k.isdigit():
        print('Введите число')
        exit()

    c, s = DigitCountSum(k)
    print(f'Количество цифр: {c}\nИх сумма: {s}\n')
