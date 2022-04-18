# 12. Сложить цифры вещественного числа
strange_number = input('Введите число ')
sum = 0

for n in strange_number:
    if n != ".":
        sum += int(n)

print(f'Сумма цифр {sum}')