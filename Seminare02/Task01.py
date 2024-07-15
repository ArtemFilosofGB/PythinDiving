"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

num = 5

string = "Строка"

tup = (5,6,7)

my_list = [1,1,2,3]
my_set = set(my_list)

dct = {}

#print(type(num),type(string),type(tup),type(my_list),type(my_set),sep='\n')

for el in (num,string,tup,my_list, my_set, dct):
    print(type(el))
    