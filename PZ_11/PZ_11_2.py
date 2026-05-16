# 2. Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний.


word = input('введите слово: ')

def generator(sim):
    for i in sim:
        yield i.upper()
print(''.join(generator(word)))