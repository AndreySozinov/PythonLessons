# 12. В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19.

def difference(spisok):
    minpart = spisok[0] - (spisok[0]) // 1
    maxpart = spisok[0] - (spisok[0]) // 1
    for number in spisok:
        if number - (number) // 1 < minpart:
            minpart = number - (number) // 1
        if number - (number) // 1 > maxpart:
            maxpart = number - (number) // 1
    print(f'min = {minpart} max = {maxpart}\ndifference = {maxpart - minpart}')

difference([1.1, 1.2, 3.1, 5.4, 10.01])