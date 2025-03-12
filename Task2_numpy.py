# Задача 2. Арифметические операции:
# Создайте два массива размером 3x3
# Заполните целыми числами от 1 до 9.
# Сложите массивы.
# Умножьте элементы первого массива на 2.
# Найдите произведение всех элементов второго массива.

import numpy as np

# ручной способ заполнения массивов данными
array_2d_a = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("Массив a:")
print(array_2d_a)

array_2d_b = np.array([[9, 8, 7],
                       [6, 5, 4],
                       [3, 2, 1]])
print("\nМассив b:")
print(array_2d_b)

'''
Автоматизированный способ. создаем массив 3х3, заполненный целыми числами от 1 до 10
array1 = np.random.randint(1, 10, size=(3, 3))
array2 = np.random.randint(1, 10, size=(3, 3))
print(array1)
print(array2)
'''

sum_array = array_2d_a + array_2d_b
print("\nСумма массивов: ")
print(sum_array)

prod_array_a = array_2d_a * 2
print("\nМассив после умножения на 2: ")
print(prod_array_a)

prod_array_b = np.prod(array_2d_b)
print("\nПроизведение всех элементов: ")
print(prod_array_b)
