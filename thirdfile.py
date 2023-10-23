lst = input("Введите список чисел через пробел: ").split()

# Проверим, что введены только цифры
allowed_chars = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in lst:
    for char in num:
        if char not in allowed_chars:
            print("Ошибка! Введите только цифры и отрицательные/положительные числа.")
            exit()

lst = [int(i) for i in lst]

# Найдем сумму положительных элементов списка
sum_pos = 0
for i in lst:
    if i > 0:
        sum_pos += i
print("Сумма положительных элементов:", sum_pos)

# Найдем сумму элементов списка после первого нуля
sum_after_zero = 0
flag = False
for i in lst:
    if i == 0:
        flag = True
    elif flag:
        sum_after_zero += i
if flag:
    print("Сумма элементов после первого нуля:", sum_after_zero)
else:
    print("Сумму посчитать нельзя")

# Удалим из списка все отрицательные элементы
lst = [i for i in lst if i >= 0]
print("Список без отрицательных элементов:", lst)