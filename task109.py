# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

expression = "11-2*300+6/2"

# Разбиваем строку с выражением на числа и знаки операций
elements = []
pos = 0
for i in range(len(expression)):
    if not expression[i].isdigit(): 
        elements.append(int(expression[pos:i]))
        pos = i+1
        elements.append(expression[i])
elements.append(expression[pos:])

print(elements)