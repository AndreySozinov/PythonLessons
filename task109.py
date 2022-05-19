# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

# Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# Задаем выражение:
expression = "11-2*300+6/2"

print(f'{expression} = ', end='')

elements = []
pos = 0

# Разбиваем строку с выражением на числа и знаки операций
for i in range(len(expression)):
    if not expression[i].isdigit(): 
        elements.append(int(expression[pos:i]))
        pos = i+1
        elements.append(expression[i])
elements.append(int(expression[pos:]))

multposition = divposition = pluspos = minuspos = len(elements)

# Сперва проверяем наличие умножения или деления
while "*" in elements or "/" in elements:
    if "*" in elements: multposition = elements.index('*')
    if "/" in elements: divposition = elements.index('/')
    # Определяем что встречается раньше - умножение или деление и выполняем его
    if multposition < divposition:
        result = elements[multposition-1] * elements[multposition+1]
        del elements[multposition-1:multposition+2]
        elements.insert(multposition-1, result)
        multposition = len(elements)
    if multposition > divposition:
        result = elements[divposition-1] / elements[divposition+1]
        del elements[divposition-1:divposition+2]
        elements.insert(divposition-1, result)
        divposition = len(elements)
# Остается выполнить сложение или вычитание в порядке встречаемости
while "+" in elements or "-" in elements:
    if "+" in elements: pluspos = elements.index('+')
    if "-" in elements: minuspos = elements.index('-')
    if pluspos < minuspos:
        result = elements[pluspos-1] + elements[pluspos+1]
        del elements[pluspos-1:pluspos+2]
        elements.insert(pluspos-1, result)
        pluspos = len(elements)
    else: 
        result = elements[minuspos-1] - elements[minuspos+1]
        del elements[minuspos-1:minuspos+2]
        elements.insert(minuspos-1, result)
        minuspos = len(elements)

print(elements[0])