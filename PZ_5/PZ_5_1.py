# С помощью функции получить вертикальную и горизонтальную линии.
# линия проводится многократной печатью символа.
# Заключить слово в рамку из полученных линий.

try:
    def word_ramka(word: str):
        print('/' + '-' * len(word) + '\\')
        print('|' + word + '|')
        print('\\' + '-' * len(word) + '/')


    word = input('Введите слово: ')
    word_ramka(word)
except  Exception as e:
    print(f"Ошибка: {e}")
