# Какой средний рейтинг фильмов по каждому жанру?
# Какие фильмы получили наибольшее количество отзывов с рейтингом 5?
# Какой процент отзывов содержит текстовые комментарии (столбец review_text не пустой)?
# В какие дни недели пользователи чаще всего оставляют отзывы?
# Сколько уникальных пользователей написали хотя бы один отзыв?

import pandas as pd
import numpy as np
from random import choice, randint
from datetime import datetime, timedelta

# Параметры для генерации данных
np.random.seed(42)  # Для воспроизводимости результатов
genres = ["Драма", "Комедия", "Боевик", "Фантастика", "Ужасы"]
movies = {
    "Драма": ["Фильм A", "Фильм B", "Фильм C"],
    "Комедия": ["Фильм D", "Фильм E", "Фильм F"],
    "Боевик": ["Фильм G", "Фильм H", "Фильм I"],
    "Фантастика": ["Фильм J", "Фильм K", "Фильм L"],
    "Ужасы": ["Фильм M", "Фильм N", "Фильм O"]
}
users = [f"user_{i}" for i in range(1, 51)]  # 50 уникальных пользователей
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Генерация данных
data = []
for _ in range(1000):  # 1000 отзывов
    genre = choice(genres)
    movie = choice(movies[genre])
    rating = randint(1, 5)  # Рейтинг от 1 до 5
    user = choice(users)
    review_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    has_text = np.random.choice([True, False], p=[0.7, 0.3])  # 70% отзывов с текстом
    review_text = f"Отзыв на {movie}" if has_text else None

    data.append({
        "user_id": user,
        "movie_title": movie,
        "genre": genre,
        "rating": rating,
        "review_date": review_date.strftime("%Y-%m-%d"),
        "review_text": review_text
    })

# Создание DataFrame и сохранение в CSV
df_reviews = pd.DataFrame(data)
df_reviews.to_csv("movie_reviews.csv", index=False)

# Считывание из файла
file_path = 'movie_reviews.csv'
df_reviews = pd.read_csv(file_path)

# Какой средний рейтинг фильмов по каждому жанру?

# 1. Вычисление среднего рейтинга фильмов по каждому жанру
average_rating_by_genre = df_reviews.groupby('genre')['rating'].mean()
# 2. Сортировка по убыванию для лучшей визуализации
average_rating_by_genre_sorted = average_rating_by_genre.sort_values(ascending=False)
# 3. Вывод результата
print("Средняя оценка рейтинга по жанрам:")
print(average_rating_by_genre_sorted)

# Какие фильмы получили наибольшее количество отзывов с рейтингом 5?

# 1. Фильтрация по рейтингу
filtered_rating5 = df_reviews[df_reviews['rating'] == 5]
# 2. Группировка по фильму и жанру с подсчетом отзывов
reviews_films_rating5 = filtered_rating5.groupby('movie_title')['rating'].count()
# 3. Сортировка по убыванию
reviews_films_sorted = reviews_films_rating5.sort_values(ascending=False)
# 4. Вывод результата
print("\nФильмы с наибольшим количеством отзывов с рейтингом 5:")
print(reviews_films_sorted)

# Какой процент отзывов содержит текстовые комментарии (столбец review_text не пустой)?

# 1. Проверка на наличие пустых значений
reviews_with_text = df_reviews['review_text'].notnull()
# 2. Подсчет отзывов всего и количества отзывов с текстом
total_reviews = len(df_reviews)
reviews_with_text_count = reviews_with_text.sum()
# 3. Проценты отзывов с текстовыми комментариями
percent_with_text = (reviews_with_text_count / total_reviews) * 100
# 4. Вывод результата
print(f"\nПроцент отзывов, содержащих текстовые комментарии: {percent_with_text:.2f}%")

# В какие дни недели пользователи чаще всего оставляют отзывы?

# 1. Преобразование в формат даты
df_reviews['review_date'] = pd.to_datetime(df_reviews['review_date'])
# 2. Извлечения дня недели из даты
df_reviews['day_of_week'] = df_reviews['review_date'].dt.dayofweek
# 3. Подсчет количества отзывов
review_by_day = df_reviews.groupby('day_of_week').size()
# 4. Сортировка по убыванию
review_by_day_sorted = review_by_day.sort_values(ascending=False)
# 5. Преобразование числовых дней недели в читаемый формат
day_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
review_by_day_sorted.index = review_by_day_sorted.index.map(lambda x: day_names[x])
# 6. Вывод результата
print("\nЧастые отзывы, оставленные пользователями по дням недели:")
print(review_by_day_sorted)

# Сколько уникальных пользователей написали хотя бы один отзыв?

# 1. Отбор уникальных пользователей
unique_clients = df_reviews['user_id'].nunique()
# 2. Вывод результата
print(f"\nКоличество пользователей, которые написали хотя бы 1 отзыв: {unique_clients}")

