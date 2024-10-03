import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(5)  # массив из 5 случайных чисел по оси X
y = np.random.rand(5)  # массив из 5 случайных чисел по оси Y

# Вывод сгенерированных массивов
print("Массив X:", x)
print("Массив Y:", y)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7)

# Настройка заголовка и меток
plt.title('Диаграмма рассеяния двух наборов данных', fontsize=16)
plt.xlabel('Ось X', fontsize=14)
plt.ylabel('Ось Y', fontsize=14)

# Сохранение диаграммы в файл
plt.savefig('Диаграмма_Задача_2.jpg')

# Показываем график
plt.show()
