import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# Фиксация seed для воспроизводимости
np.random.seed(42)

# Параметры генерации данных
num_orders = 1000  # Количество заказов
start_date = datetime(2022, 1, 1)  # Начальная дата
end_date = datetime(2023, 1, 1)  # Конечная дата

# Генерация случайных данных
data = {
    'order_id': range(1, num_orders + 1),  # Уникальный идентификатор заказа
    'customer_id': np.random.randint(1, 501, size=num_orders),  # Уникальный идентификатор клиента (1-500)
    'order_date': [
        start_date + timedelta(days=np.random.randint(0, 365))
        for _ in range(num_orders)
    ],  # Случайная дата между start_date и end_date
    'order_amount': np.random.uniform(100, 5000, size=num_orders).round(2),  # Сумма заказа от 100 до 5000
    'platform': np.random.choice(['mobile', 'desktop'], size=num_orders),  # Случайная платформа
    'category': np.random.choice(['smartphones', 'laptops'], size=num_orders)  # Случайная категория
}

# Создание DataFrame
df_orders = pd.DataFrame(data)

# Преобразование даты в строковый формат
df_orders['order_date'] = df_orders['order_date'].dt.strftime('%Y-%m-%d')

# Сохранение данных в CSV
df_orders.to_csv('orders.csv', index=False)

print("Файл orders.csv успешно создан.")

print()   

# Задача: Написать код, который выполняет следующие действия:

#1. Выделить клиентов , совершивших первую покупку в течение определённого месяца (когорту).
#2. Рассчитать размер каждой когорты .
#3. Вычислить средний доход с клиента для каждой когорты за 10 дней от момента их первой покупки .
#4. Отобразить результаты по месяцам первых покупок, категориям товаров и платформам .
# Ожидаемый результат:
# Таблица с полями:
# Дата когорты (дата первой покупки клиента)
# Платформа
# Категория товара
# Размер когорты
# Средний доход с клиента

df_orders = pd.read_csv('Task_pandas/orders.csv')
print(df_orders)

print()

# Преобразуем столбец в дата формат
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

# Сделаем группировку по customer_id и отфильтруем по минимальному значению
first_date_df = df_orders.groupby('customer_id', as_index=False).agg({'order_date': 'min'}).rename(columns=({'order_date': 'first_order_date'}))
print(first_date_df)

print()

# Добавление столбца cohort_month. Преобразуем дату в период (месяц) и обратно в timestamp до 1 дня
first_date_df['cohort_month'] = first_date_df['first_order_date'].dt.to_period('M').dt.to_timestamp()
print(first_date_df)

print()

# Добавили ко всей таблице 
df_orders = df_orders.merge(first_date_df, on='customer_id')
print(df_orders)

print()

# Фильтрация данных за 10 дней после первой покупки
df_orders['days_delta'] = (df_orders['order_date'] - df_orders['first_order_date']).dt.days
print(df_orders)

print()

filtered_first_days_10_orders = df_orders[df_orders['days_delta'] < 10]
print(filtered_first_days_10_orders)

print()

# Группировка данных по customer_id и cohort_month, агрегация суммы заказов
total_customer_amount_df = (
    df_orders[['customer_id', 'order_amount', 'cohort_month', 'platform', 'category']] # Выбор нужных столбцов
    .groupby(['customer_id', 'cohort_month', 'platform', 'category'], as_index=False) # Группировка по двум столбцам
    .agg({'order_amount': 'sum'}) # Суммирование по столбцу order_amount
    .rename(columns=({'order_amount': 'total_customer_amount'})) # Переименование столбца
)
print(total_customer_amount_df)

print()

# Группировка по cohort_date, затем нахождение среднего значения по столбцу total_customer_amount_df и уникальных пользователей по столбцу customer_id
cohort_month_df = (
    total_customer_amount_df.groupby(['cohort_month', 'platform', 'category'], as_index=False)
    .agg({'total_customer_amount': 'mean', 'customer_id': pd.Series.nunique})
)
print(cohort_month_df)
