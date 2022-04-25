# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

n = int(input('Введите число N: '))

list = list(range(1, n + 1))

for i in range(1, n):
    list[i] = list[i-1] * list[i]

print(list)