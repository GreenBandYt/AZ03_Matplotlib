import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0          # Среднее значение
std_dev = 1       # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

# Настройка заголовка и меток
plt.title('Гистограмма нормального распределения', fontsize=16)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Частота', fontsize=14)

# Отображение графика
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

# Сохранение гистограммы в файл
plt.savefig('Гистограмма_Задача_1.jpg')

plt.show()
