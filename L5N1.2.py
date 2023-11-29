import numpy as np

# Создание матрицы X
X = np.ones((12, 3))
X[:, 1] = np.random.randint(12, 25, size=12)
X[:, 2] = np.random.randint(60, 83, size=12)

# Создание вектора Y
Y = np.random.uniform(13.5, 18.6, size=12)

# Вычисление оценок уравнения регрессии
A = np.linalg.inv(X.T @ X) @ X.T @ Y

# Проверка полученных значений Y
Y_predicted = X @ A

print("Оценки A:")
print(A)
print()
print("Проверка значений Y:")
print("Полученные значения Y:")
print(Y_predicted)
print()
print("Исходные значения Y:")
print(Y)
