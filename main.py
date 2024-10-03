import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL для парсинга
url = "https://www.divan.ru/smolensk/category/divany-i-kresla"

# Выполняем HTTP-запрос к сайту
response = requests.get(url)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы с ценами
    price_elements = soup.find_all('span', class_='ui-LD-ZU KIkOH')

    # Извлекаем текст цен и сохраняем в список
    prices_raw = [price.text.strip() for price in price_elements if price.text.strip()]

    # Сохраняем сырые данные в CSV файл
    raw_df = pd.DataFrame(prices_raw, columns=['Raw Price'])
    raw_df.to_csv('price_site.csv', index=False)
    print("Сырые данные успешно спарсены и сохранены в price_site.csv")

    # Обработка цен: очистка и преобразование в целые числа
    prices = []
    for price in prices_raw:
        # Удаляем символы, которые не являются цифрами
        cleaned_price = ''.join(filter(str.isdigit, price))
        if cleaned_price:  # Проверяем, что строка не пустая
            prices.append(int(cleaned_price))

    # Сохраняем очищенные цены в DataFrame
    df = pd.DataFrame(prices, columns=['Price'])
    df.to_csv('sofa_prices.csv', index=False)
    print("Цены успешно очищены и сохранены в sofa_prices.csv")

    # Вычисление средней цены
    average_price = df['Price'].mean()
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")

    # Построение гистограммы цен
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество диванов')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('sofa_price_histogram.png')  # Сохранить гистограмму
    plt.show()
else:
    print("Ошибка при выполнении запроса:", response.status_code)
