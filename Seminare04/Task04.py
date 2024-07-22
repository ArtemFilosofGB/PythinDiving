"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

import random
from pprint import pprint
from timeit import timeit

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [random.randint(-100, 100) for i in range(1000)]
pprint(lst)
print(bubble_sort(lst))
print(timeit(lambda: bubble_sort(lst), number=1000))