"""Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""

def string_to_dict(string):
    string = string.split()
    min_num = int(string[0])
    max_num = int(string[1])
    result = {}
    for i in range(min_num, max_num + 1):
        result[chr(i)] = i
    return result

def string_to_dicti(string):
    return {chr(int(i)): int(i) for i in string.split()}

txt = "55 78869"
print(string_to_dict(txt))