# задача повышенной сложности 1:
# какая общая выручка магазина за год? (подсказка: используйте формулу price * quantity.) (выполнено)
# какие категории товаров приносят наибольшую выручку? (Выполнено)
# какое количество уникальных клиентов совершили покупки? (Выполнено)
# в какой месяц было больше всего заказов? (Выполнено)
# найдите топ-5 самых популярных товаров по количеству продаж. (Выполнено)

import pandas as pd
import numpy as np
from random import choice, randint
from datetime import datetime, timedelta

# параметры для генерации данных
np.random.seed(42)  # для воспроизводимости результатов
categories = ["электроника", "одежда", "бытовая техника", "книги", "игрушки"]
products = {
    "электроника": ["смартфон", "ноутбук", "наушники", "планшет"],
    "одежда": ["футболка", "джинсы", "куртка", "обувь"],
    "бытовая техника": ["холодильник", "пылесос", "микроволновка", "кофеварка"],
    "книги": ["роман", "научная литература", "фэнтези", "детектив"],
    "игрушки": ["конструктор", "кукла", "машинка", "пазл"]
}
customers = [f"customer_{i}" for i in range(1, 101)]  # 100 уникальных клиентов
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# генерация данных
data = []
for _ in range(1000):  # 1000 заказов
    category = choice(categories)
    product = choice(products[category])
    price = randint(10, 1000)  # цена от 10 до 1000
    quantity = randint(1, 5)  # количество от 1 до 5
    customer = choice(customers)
    order_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))

    data.append({
        "order_id": len(data) + 1,
        "product_name": product,
        "category": category,
        "price": price,
        "quantity": quantity,
        "order_date": order_date.strftime("%y-%m-%d"),
        "customer_id": customer
    })

# создание dataframe и сохранение в csv
df_sales = pd.DataFrame(data)
df_sales.to_csv("sales_data.csv", index=False)
print(df_sales.head())

# считывание с файла
file_path = 'sales_data.csv'
df_sales = pd.read_csv('sales_data.csv')

# (+) какая общая выручка магазина за год?
df_sales['revenue'] = df_sales['price'] * df_sales['quantity']
total_sales_sum = df_sales['revenue'].sum()
print(f"\nОбщая выручка компании за год: {total_sales_sum}")

# (+) какие категории товаров приносят наибольшую выручку?
category_revenue = df_sales.groupby('category')['revenue'].sum()
category_revenue_sorted = category_revenue.sort_values(ascending=False)
print("\nКатегории товаров, приносящие наибольшую выручку:")
print(category_revenue_sorted)

# (+) какое количество уникальных клиентов совершили покупки?
unique_clients = df_sales['customer_id'].nunique()
print(f"\nУникальные клиенты, совершившие покупку: {unique_clients}")

# (+) в какой месяц было больше всего заказов?
# 1. Преобразовали столбец в формат даты
df_sales['order_date'] = pd.to_datetime(df_sales['order_date'])

# 2. Извлекли месяц из даты заказа
df_sales['month'] = df_sales['order_date'].dt.month

# 3. Сгруппировали данные по месяцам и подсчитали количество заказов
orders_by_month = df_sales.groupby('month')['order_id'].count()

# 4. Нашли месяц с максимальным количеством заказа
max_orders_month = orders_by_month.idxmax()
max_orders_count = orders_by_month.max()

# 5. Вывели результат на экран
print(f"\nМесяц с максимальными заказами:{max_orders_month} (количество заказов всего: {max_orders_count})")

# (+) найдите топ-5 самых популярных товаров по количеству продаж.
# 1. Сгруппируйте данные по названию товара (product_name) и просуммируйте количество продаж (quantity).
product_sales = df_sales.groupby('product_name')['quantity'].sum()

# 2. Отсортируйте товары по убыванию количества продаж.
product_sales_sorted = product_sales.sort_values(ascending=False) # Сортировка товара по убыванию

# 3. Выведите топ-5 товаров.
top5_product = product_sales_sorted.head(5)
print("\nТоп-5 самых популярных товаров по количеству продаж:")
print(top5_product)
