class String:
    def __init__(self, value):
        self.value = value
    def length(self):
        return len(self.value)
    def uppercase(self):
        return self.value.upper()
    def lowercase(self):
        return self.value.lower()
    def reverse(self):
        return self.value[::-1]
    def count_characters(self):
        characters = {}
        for char in self.value:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        return characters

    def __str__(self):
        return self.value

# Пример использования класса String
s = String("Привет, Мир!")
print("Исходная строка:", s)
print("Длина строки:", s.length())
print("Строка в верхнем регистре:", s.uppercase())
print("Строка в нижнем регистре:", s.lowercase())
print("Перевёрнутая строка:", s.reverse())
print("Количество разных символов:", s.count_characters())