# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input("Введите число членов последовательности: "))
list = list(range(1, n + 1))

for index in range(1, n):
    list[index] = list[index - 1] * -3

print(list)