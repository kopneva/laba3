
# Открываем файл для чтения
with open('Предметы.txt', 'r') as file:
    # Создаем пустой словарь
    subjects_dict = {}

    # Читаем содержимое файла построчно
    for line in file:
        # Разделяем строку на название предмета и информацию о занятиях
        parts = line.strip().split(':')

        # Извлекаем название предмета и удаляем пробелы
        subject = parts[0].strip()

        # Извлекаем информацию о занятиях и разделяем ее на отдельные элементы
        lessons_info = parts[1].strip().split()

        # Вычисляем общее количество занятий
        total_lessons = sum(int(info.split('(')[0]) for info in lessons_info)

        # Добавляем предмет и общее количество занятий в словарь
        subjects_dict[subject] = total_lessons

# Выводим словарь на экран
print(subjects_dict)