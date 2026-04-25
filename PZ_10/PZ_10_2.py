# 2. Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open('text18-5.txt', encoding='UTF-8') as f1:
    content = f1.read()
print('Содержимое файла:')
print(content)
print('\n')
print('количество символов в тексте:')
print(len(content))

with open('text18-5.txt', encoding='UTF-8') as f:
    lines = f.readlines()

with open('new_poem.txt', 'w', encoding='UTF-8') as f_out:
    for line in lines:
        upper_line = line.upper()
        f_out.write(upper_line)
