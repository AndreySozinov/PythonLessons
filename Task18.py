# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

dict = {}
n = int(input('Введите натуральное n: '))

for k in range(1, n + 1):
    dict[k] = 3 * k + 1

print(dict)
