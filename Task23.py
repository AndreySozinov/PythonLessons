# Найти сумму чисел списка стоящих на нечетной позиции

list = [5, 88, 3, 6, 11, 15, 9, 5]

sum = 0

for i in range(0, len(list), 2):
    sum += list[i]

print(sum)