while True:
    try:
        x = int(input("Введите число: "))
        result = 10 / x
        print("Результат: ", result)
        break
    except ValueError:
        print("Ошибка! Введено некорректное значение. Попробуйте ещё раз.")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль. Попробуйте ещё раз.")
    finally:
        print("Программа завершена.")