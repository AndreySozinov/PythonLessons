# 2. Найти максимальное из пяти чисел
from random import randint

list = []
i = 0

while i < 5:
    list.append(randint(0, 100))
    print(list[i], end=' ')
    i += 1

max = list[0]
for number in list:
    if number > max: max = number

print(f'\nМаксимальное число {max}')