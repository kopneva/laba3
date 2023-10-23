def count_letter_pairs_and_vowels(word):
    upper_pairs = 0
    lower_pairs = 0
    vowels = 0

    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]

        if current_char.isalpha() and next_char.isalpha():
            if current_char.isupper() == next_char.isupper():
                if current_char.isupper():
                    upper_pairs += 1
                else:
                    lower_pairs += 1

        if current_char.lower() in 'aeyiouаеоыиюяэ':
            vowels += 1

    return upper_pairs, lower_pairs, vowels

# Пример использования
word = input("Введите слово: ")
upper_pairs, lower_pairs, vowels = count_letter_pairs_and_vowels(word)

print(f"Пары верхнего регистра: {upper_pairs}")
print(f"Пары нижнего регистра: {lower_pairs}")
print(f"Гласных букв: {vowels}")