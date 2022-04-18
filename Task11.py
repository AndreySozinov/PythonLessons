number = 0
list = []
while number != 554:
    number = int(input('Введите число '))
    if number % 2 != 0:
        list.append(number)
print(list)