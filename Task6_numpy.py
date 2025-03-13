# Задача 12. Сортировка и выборка
# Создайте массив из 20 случайных чисел от 0 до 100.
# Отсортируйте его по возрастанию.
# Выберите первые 5 элементов.
# Выберите последние 5 элементов.
import numpy as np

array = np.random.randint(100, size=20)
print(f"\nСлучайный массив из 20 чисел от 0 до 100: {array}")

sort_array = np.sort(array)
print(f"Отсортированный массив: {sort_array}")

slicing_array_first5 = sort_array[:5]
print(f"\nПервые 5 элементов: {slicing_array_first5}")

slicing_array_last5 = sort_array[-5:]
print(f"Последние 5 элементы: {slicing_array_last5}")
