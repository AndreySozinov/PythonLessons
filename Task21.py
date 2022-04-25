# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

path = "file21.txt"
position = open(path, 'w')
position.writelines('2\n')
position.writelines('5\n')
position.writelines('3\n')
position.writelines('10')
position.close()

n = int(input("Введите число N: "))

list = list(range(-n, n + 1))
print(list)

multi = 1
position = open(path, 'r')
for line in position:
    multi *= list[int(line)]
position.close()

print(multi)