"""
Задание №9
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
"""


for i in  range(2,10,5):
    for j in range(2,11):
        print(f"{i}x{j}={i*j}\t{i+1}x{j}={(i+1)*j}\t{i+2}x{j}={(i+2)*j}\t{i+3}x{j}={(i+3)*j}")
    print()

# for k in [0, 4]:
#     for i in range(2, 11):
#         result = ''
#         for j in range(2 + k, 6 + k):
#             result += f'{j:^2} x {i:^2} = {i * j:^2}\t'
#         print(result)
#     print()