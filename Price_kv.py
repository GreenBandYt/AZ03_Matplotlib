import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('prices.csv')

# Удаление символов '₽/мес.' и преобразование в числовой тип
df['Цена'] = df['Цена'].str.replace('₽/мес.', '').str.replace(' ', '').astype(int)

# Сохранение обработанных данных обратно в CSV
df.to_csv('processed_prices.csv', index=False, encoding='utf-8')

print("Данные успешно обработаны и сохранены в processed_prices.csv.")
