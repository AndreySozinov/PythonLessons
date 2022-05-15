# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую 
# последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#         [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

list = [1, 5, 2, 3, 4, 6, 1, 7]

maxcount = 0
startpos = 0
for i in range(len(list)): # находим позицию числа справа от которого большинство чисел больше этого числа
    count = 0
    for j in range(i + 1, len(list)):
        if list[i] < list[j]:
            count += 1
    if maxcount < count: 
        maxcount = count
        startpos = i

result = []

for i in range(startpos, len(list)-1): # находим наибольшую возрастающую последовательность
    temp = [list[startpos]]
    for j in range(i+1, len(list)):
        if list[j] > max(temp):
            temp.append(list[j])
    if len(temp) > len(result): result = temp.copy()
    del temp[:]

print(result)

