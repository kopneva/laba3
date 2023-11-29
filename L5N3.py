import numpy as np
import matplotlib.pyplot as plt

# Задание интервала и дельты t
t = np.arange(2, 3, 0.05)

# Вычисление значений функции
s = np.log(np.abs(1.3 + t)) - np.exp(t)

# Вывод значений аргумента и значения функции
for i in range(len(t)):
    print("t =", t[i], "f(t) =", s[i])

# Нахождение наибольшего, наименьшего и среднего значения
maximum = np.max(s)
minimum = np.min(s)
average = np.mean(s)

print("Максимальное значение:", maximum)
print("Минимальное значение:", minimum)
print("Среднее значение:", average)

length = len(s)
sorted_array = np.sort(s)

print("Количество элементов:", length)
print("Отсортированный массив:", sorted_array)

# Построение графика
plt.plot(t, s, marker='o', label='f(x)')

# Построение графика прямой среднего значения
plt.axhline(average, color='r', linestyle='--', label='Average')

# Настройка осей и пределов
plt.xlabel('t')
plt.ylabel('f(t)')
plt.xlim([2, 3])
plt.ylim([-10, 10])

# Легенда
plt.legend()

# Отображение графика
plt.show()

# Построение графика прямой среднего значения
plt.plot(t, np.full_like(t, average), marker='s', label='Average')

# Настройка осей и пределов
plt.xlabel('t')
plt.ylabel('f(t)')
plt.xlim([2, 3])
plt.ylim([-10, 10])

# Легенда
plt.legend()

# Отображение графика
plt.show()