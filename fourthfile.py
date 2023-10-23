# Ввод ключей и значений с клавиатуры
d = {}
n = int(input("Введите количество элементов в словаре: "))
for i in range(n):
    key = input("Введите ключ: ")
    value = int(input("Введите значение: "))
    d[key] = value

# Сортировка по возрастанию значений
sorted_d_asc = sorted(d.items(), key=lambda x: x[1])
print("Словарь, отсортированный по возрастанию значений:", dict(sorted_d_asc))

# Сортировка по убыванию значений
sorted_d_desc = sorted(d.items(), key=lambda x: x[1], reverse=True)
print("Словарь, отсортированный по убыванию значений:", dict(sorted_d_desc))