# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input('k = ?\n'))

polynomial1 = ""
polynomial2 = ""

coeff = [randint(0, 10) for x in range(k + 1)]
#polynomial1 = "".join(f'{coeff[i]}x^{k - i} + ' for i in range(0, k - 1) if coeff[i] != 0) + f'{coeff[-2]}x + {coeff[-1]} = 0'
for i in range(0, k - 1):
    if coeff[i] > 1:
        polynomial1 = polynomial1 + f'{coeff[i]}x^{k - i} + '
    elif coeff[i] == 1:
        polynomial1 = polynomial1 + f'x^{k - i} + '
if coeff[k - 1] > 1:
    polynomial1 = polynomial1 + f'{coeff[k - 1]}x'
elif coeff[k - 1] == 1:
    polynomial1 = polynomial1 + f'x'
if coeff[k] != 0:
    polynomial1 = polynomial1 + f' + {coeff[k]} = 0'

print(polynomial1)

# coeff = [randint(0, 10) for x in range(k + 1)]
# #polynomial2 = "".join(f'{coeff[i]}x^{k - i} + ' for i in range(0, k - 1) if coeff[i] != 0) + f'{coeff[-2]}x + {coeff[-1]} = 0'
# print (f'{polynomial1}\n{polynomial2}')

# file = open('file.txt', 'w')
# file.write(f'{polynomial1}\n')
# file.write(polynomial2)
# file.close