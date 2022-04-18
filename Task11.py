# 11. Напишите программу, которая выводит нечетные числа 
# из заданного списка и останавливается, если встречает число 554.

number = 0
list = []
while number != 554:
    number = int(input('Введите число '))
    if number % 2 != 0:
        list.append(number)
print(list)