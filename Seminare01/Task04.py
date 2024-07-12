"""Задание №7
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print"""
result = None
while (1):
    number = int(input("Введите число от 1 до 999: "))
    if number==0:
        break
    if number > 999 or number<1:
        print("Неверный ввод")
        continue
    elif 1<= number < 10:
        result = number ** 2
        print(f"Result: {result}")
    elif 10<= number < 100:
        result = number % 10 * number // 10
        print(f"Result: {result}")
    elif 100<=number < 1000:
        last = number % 10
        number //= 10
        middle = number % 10
        first = number // 10
        result = last * 100 + middle * 10 + first
    print(result)
