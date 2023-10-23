while True:
    try:
        x = int(input("Введите натуральное число: "))
        if x <= 0:
            print("Число должно быть больше 0")
        else:
            break
    except ValueError:
        print("Некорректный ввод, попробуйте еще раз")
result = 'Последовательность цифр упорядочена по убыванию'
while x // 10 != 0:
    x, n = divmod(x, 10)
    if n >= x % 10:
       result = 'Последовательность цифр  не упорядочена по убыванию'
       break
print(result)