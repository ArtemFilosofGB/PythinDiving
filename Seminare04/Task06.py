"""Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

def sum_range(lst, start, end):
    if start < 0:
        start = 0
    if end > len(lst) - 1:
        end = len(lst) - 1
    return sum(lst[start:end + 1])


lst = [1, 2, 3, 4, 5]
start = 2
end = 4
print(sum_range(lst, start, end))


"""num_list = [1, 5, 7, -9, 0]


def sunnator(num_list: list[int], index_1: int, index_2: int):
    if index_1 > index_2:
        return 0

    return sum(num_list[max(index_1, 0):min(index_2 + 1, len(num_list))])


print(sunnator(num_list, -3, 10))"""