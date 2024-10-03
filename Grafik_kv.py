import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('processed_prices.csv')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, color='blue', alpha=0.7, edgecolor='black')

# Настройка заголовка и меток
plt.title('Гистограмма цен', fontsize=16)
plt.xlabel('Цена (₽)', fontsize=14)
plt.ylabel('Частота', fontsize=14)

# Отображение графика
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
