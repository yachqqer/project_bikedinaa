# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы, умноженные на минимальный элемент :

num = [0, 8, 4, 2, 5, -2, -5, -7]

f2 = open('text2.txt', 'w', encoding='UTF-8')
for i in num:
    f2.write(str(i) + ' ')
f2.close()

ogo = []
xuila = (len(num))

sum = 0
min1 = min(num)
fuck = 0

for i in num:
    sum += i
    fuck = min1 * i
    ogo.append(fuck)

f1 = open('text1.txt', 'w', encoding='UTF-8')
f1.write('Исходные данные:\n')
for i in num:
    f1.write(str(i) + ' ')
f1.write('\n')
f1.write('Количество элементов:\n')
f1.write(str(xuila))
f1.write('\n')
f1.write('Сумма элементов:\n')
f1.write(str(sum))
f1.write('\n')
f1.write('Элементы, умноженные на минимальный элемент:\n')
for i in ogo:
    f1.write(str(i) + ' ')
f1.close()