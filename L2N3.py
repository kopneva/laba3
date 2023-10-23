def check_positive(matrix):
    for row in matrix:
        if not any(num > 0 for num in row):
            return False
    return True

def invert_matrix(matrix):
    inverted_matrix = []
    for row in matrix:
        inverted_row = [-num for num in row]
        inverted_matrix.append(inverted_row)
    return inverted_matrix

def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк матрицы: "))
            if rows <= 0 :
                print("Количество строк и столбцов должно быть положительным числом.")
                continue
            columns = int(input("Введите количество столбцов матрицы: "))
            if  columns <= 0:
                print("Количество строк и столбцов должно быть положительным числом.")
                continue
            matrix = []
            for i in range(rows):
                row = []
                for j in range(columns):
                    num = int(input(f"Введите элемент [{i}][{j}]: "))
                    row.append(num)
                matrix.append(row)
            return matrix
        except ValueError:
            print("Некорректный ввод данных.")

matrix = input_matrix()
if check_positive(matrix):
    inverted_matrix = invert_matrix(matrix)
    print("Инвертированная матрица:")
    for row in inverted_matrix:
        print(row)
else:
    print("Не все строки матрицы содержат положительные элементы.")