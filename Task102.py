# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def PolynomForming (power, coefficients): # Формируем многочлен
    polynomial = ""
    for i in range(0, power - 1):
        if coefficients[i] > 1:
            polynomial = polynomial + f'{coefficients[i]}x^{power - i} + '
        elif coefficients[i] == 1:
            polynomial = polynomial + f'x^{power - i} + '
    if coefficients[power - 1] > 1:
        polynomial = polynomial + f'{coefficients[power - 1]}x'
    elif coefficients[power - 1] == 1:
        polynomial = polynomial + f'x'
    else: polynomial = polynomial[:-3]
    if coefficients[power] != 0:
        polynomial = polynomial + f' + {coefficients[power]} = 0'
    else:
        polynomial = polynomial + ' = 0'
    return polynomial


k = int(input('k = ?\n'))


coeff = [randint(0, 10) for x in range(k + 1)]
polynom1 = (PolynomForming(k, coeff))

coeff = [randint(0, 10) for x in range(k + 1)]
polynom2 = (PolynomForming(k, coeff))

print(f'{polynom1}\n{polynom2}')

file = open('file.txt', 'w')
file.write(f'{polynom1}\n')
file.write(polynom2)
file.close