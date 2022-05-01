# 13. Написать программу преобразования десятичного числа в двоичное.

def numberconversion(number):
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    print(result)

numberconversion(400)