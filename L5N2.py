import pandas as pd
import matplotlib.pyplot as plt

# Загрузка датасета
dataset = pd.read_csv('test.csv')

# Взятие 1000 значений из датасета
sample = dataset.sample(n=1000, random_state=42)

# Проверка на пропуски
missing_values = sample.isnull().sum()
print(missing_values)

# Построение ящика с усами на логарифмической шкале
plt.yscale('log')
sample.boxplot()
plt.show()

# Построение гистограммы
sample.hist()
plt.show()

# Заполнение пропусков
sample_filled = sample.fillna(value)

# Обработка аномальных значений
sample_processed = sample_filled[(sample_filled['column'] > lower_threshold) & (sample_filled['column'] < upper_threshold)]

# Определение количества комнатных квартир
room_counts = sample_processed['КоличествоКомнат'].value_counts()
print(room_counts)

# Построение сводной таблицы
pivot_table = pd.pivot_table(sample_processed, values='Количество', index='Район', columns='КоличествоКомнат', aggfunc=len)
print(pivot_table)