import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        for letter in self.letters:
            print(letter)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__("En", string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."


# Создание экземпляра класса Alphabet
alphabet = Alphabet("Any", ['A', 'B', 'C'])

# Вывод букв алфавита
alphabet.print_letters()

# Вывод количества букв
print(alphabet.letters_num())

# Создание экземпляра класса EngAlphabet
eng_alphabet = EngAlphabet()

# Проверка, является ли буква "A" английской
print(eng_alphabet.is_en_letter("A"))

# Вывод количества букв в английском алфавите
print(eng_alphabet.letters_num())

# Вывод примера текста на английском языке
print(EngAlphabet.example())