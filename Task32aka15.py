# 15. Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел.

def minmax(string):
    list = string.split(' ')
    min = list[0]
    max = list[0]
    for number in list:
        if number < min: min = number
        if number > max: max = number
    print(f'min = {min}; max = {max}')

minmax('5 2 63 55 1 0')