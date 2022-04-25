# Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму

n = int(input("Введите число N: "))

list1 = []
sum = 0

for i in list(range(1, n + 1)):
    list1.append((1 + 1 / i) ** i)
    sum = sum + list1[i - 1]

print(round(sum, 3))