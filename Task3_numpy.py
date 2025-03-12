# Создайте массив из 20 случайных чисел от 0 до 100.
# Среднее значение.
# Медиану.
# Стандартное отклонение.
# Количество элементов, которые находятся в диапазоне от 20 до 80.

import numpy as np

array = np.random.randint(0, 101, size=20)
print("Массив от 1 до 100")
print(array)

# Среднее значение
mean_value = np.mean(array)
print("\nСрeднее значение: ")
print(mean_value)

# Медиана
median_value = np.median(array)
print("\nМедиана: ")
print(median_value)

# Среднее отклонение
std_value = np.std(array)
print("\nСреднее отклонение: ")
print(std_value)

# Количество элементов в промежутке от 20 до 80
filtered_elements = array[(array >= 20) & (array <= 80)]
print(f"\nДиапазон от 20 до 80: {filtered_elements}")

count_elements = len(filtered_elements)
print(f"\nКоличество элементов от 20 до 80: {count_elements}")

'''
# Альтернативный вариант подсчета элементов
count_sum_elements = ((array >= 20) & (array <= 80)).sum()
print(f"\nКоличество элементов от 20 до 80: {count_sum_elements}")
'''
