# 6. Реализовать алгоритм перемешивания списка.

from random import randint

list1 = list(range(0, 21, 2)) # Исходный список с шагом 2, чтобы интереснее было.
list2 = []
index = 0

print(list1)

while len(list2) < len(list1):
    index = randint(0, len(list1) - 1) # случайный индекс списка list1
    if list1[index] not in list2: # проверка на уже записанные элементы
        list2.append(list1[index])

print(list2)

# Хотя можно перемешивать в одном списке с помошью кортежей.