# Мастям игральных карт присвоены порядковые номера: 1- пики, 2 - трефы,
# 3 - бубны, 4 - червы. Достоинству карт, старших десятки,
# присвоены номера: 11 - валет, 12 - дама, 13 - король, 14 - туз.
# Дано трехзначное число, в котором первая цифра указывает на масть,
# а вторые две на достоинство карты. Вывести соответствующее название
# карты вида «дама червей», «туз треф» и т.п.

num = int(input("Введите трехзначное число: "))

if num < 100 or num > 999:
    print("Ошибка: нужно ввести трехзначное число")
else:
    suit_num = num // 100
    value_num = num % 100

    if suit_num == 1:
        suit_name = "пик"
    elif suit_num == 2:
        suit_name = "треф"
    elif suit_num == 3:
        suit_name = "бубен"
    elif suit_num == 4:
        suit_name = "червей"
    else:
        suit_name = None


    if suit_name is None:
        print("Ошибка: номер масти должен быть от 1 до 4")
    elif value_num < 2 or value_num > 14:
        print("Ошибка: достоинство карты должно быть от 2 до 14")
    else:

        if value_num == 11:
            value_name = "валет"
        elif value_num == 12:
            value_name = "дама"
        elif value_num == 13:
            value_name = "король"
        elif value_num == 14:
            value_name = "туз"
        else:
            value_name = str(value_num)


        card_name = f"{value_name} {suit_name}"
        print(card_name)