# 1. По двум заданным числам проверить является ли одно квадратом второго
a = int (input('Введите 1-ое число\n'))
b = int (input('Введите 2-ое число\n'))
if a == b**2 or b == a**2:
    print('Одно из чисел является квадратом другого')
else:
    print('Ни одно из чисел не является квадратом другого')