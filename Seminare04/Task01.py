"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

setence = "Шла Саша по шоссе и сосала сушку"

def print_sentence(sentence):
    for i, word in enumerate(sorted(sentence.split(), key = lambda x: len(x))):
        print(f"{i + 1:2}. {word:>{len(max(sentence.split(), key = lambda x: len(x))) + 1}}")


print_sentence(setence)


"""

def form_sentence(sentence):
    sentence_split = sorted(sentence.lower().split())
    max_len = len(max(sentence_split, key=len))
    for index, value in enumerate(sentence_split, 1):
        print(f"{index}. {value:>{max_len}} ")


form_sentence(sentence)

"""