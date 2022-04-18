string = 'What a beautiful world!'
symbol = 'a'
sum = 0

for char in string:
    if char == symbol: sum += 1

print(f'Символ "{symbol}" встречается {sum} раз(а)')