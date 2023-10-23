def process_input(data):
    if isinstance(data, list):
        data = remove_zeroes(data)
        return sum_after_last_positive(data)
    elif isinstance(data, dict):
        return get_min_value_element(data)
    elif isinstance(data, int):
        return reverse_number(data)
    elif isinstance(data, str):
        return count_words(data)
    else:
        return "Неподдерживаемый тип данных"

def remove_zeroes(lst):
    return [x for x in lst if x != 0]

def sum_after_last_positive(lst):
    last_positive_index = -1
    for i in range(len(lst)):
        if lst[i] > 0:
            last_positive_index = i
    if last_positive_index >= 0:
        return sum(lst[last_positive_index+1:])
    else:
        return 0

def get_min_value_element(dictionary):
    return min(dictionary, key=dictionary.get)

def reverse_number(number):
    return int(str(number)[::-1])

def count_words(string):
    words = string.split()
    return len(words)
def input_data():
    while True:
        try:
            data = input("Введите данные: ")
            if data.startswith("[") and data.endswith("]"):
                data = eval(data)
                if isinstance(data, list):
                    return data
                else:
                    print("Некорректный ввод списка.")
                    continue
            elif data.startswith("{") and data.endswith("}"):
                data = eval(data)
                if isinstance(data, dict):
                    return data
                else:
                    print("Некорректный ввод словаря.")
                    continue
            elif data.isdigit():
                return int(data)
            else:
                return data
        except (SyntaxError, NameError):
            print("Некорректный ввод данных.")

data = input_data()
print(process_input(data))