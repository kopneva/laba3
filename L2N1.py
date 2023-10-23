def is_anagram(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False

def input_word():
    while True:
        word = input("Введите слово: ")
        if word.isalpha():
            return word
        else:
            print("Введите только буквы, пожалуйста.")

word1 = input_word()
word2 = input_word()

if is_anagram(word1, word2):
    print("Это анаграммы")
else:
    print("Это не анаграммы")