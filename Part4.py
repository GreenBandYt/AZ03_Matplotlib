from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Создание экземпляра драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get('https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')

    # Ожидание появления элементов цен
    prices = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[@data-mark='MainPrice']/span"))
    )

    # Открытие файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена'])  # Заголовок столбца

        # Запись цен в файл
        for price in prices:
            writer.writerow([price.text])

    print("Цены успешно сохранены в prices.csv.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()
