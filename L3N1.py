import re

# Создание и запись данных в файл F1
with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if line == "":
            break
        f1.write(line + "\n")

# Копирование строк без цифр в файл F2
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        if not re.search(r'\d', line):
            f2.write(line)

# Подсчет количества слов в последней строке файла F2
with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    last_line = lines[-1].strip()
    word_count = len(last_line.split())

print("Количество слов в последней строке файла F2:", word_count)