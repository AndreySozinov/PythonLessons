# 3. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

def PolySum(list1, list2):
    result = ""
    if len(list1) > len(list2): length = len(list1)
    else: length = len(list2) # находим длину самого длинного списка
    i = 0
    j = 0
    while i < length and j < length: # перебираем элементы списков
        # проверяем, что в элементе есть х и что есть коэффициенты
        if ('x' in list1[i] or 'x' in list2[j]) and list1[i][-1] != 'x' and list2[j][-1] != 'x':
            # если степени равны складываем коэффициенты (если коэффициента нет прибавляем 1)
            if list1[i][list1[i].index('^'):] == list2[j][list2[j].index('^'):]: 
                if list1[i].index('x') > 0:
                    a = int(list1[i][:list1[i].index('x')])
                else: a = 1
                if list2[j].index('x') > 0:
                    b = int(list2[j][:list2[j].index('x')])
                else: b = 1
                member = a + b # складываем коэффициенты и записываем в строку
                result = result + str(member) + list1[i][list1[i].index('x'):] + ' + '
                i += 1
                j += 1
            # если же степени не равны, дописываем в строку элемент с большей степенью
            elif list1[i][list1[i].index('^'):] > list2[j][list2[j].index('^'):]:
                result = result + list1[i] + ' + '
                i += 1
            else: 
                result = result + list2[j] + ' + '
                j += 1
        else: # проверка на наличие х и наличие коэффициента если степени нет
            if 'x' in list1[i]: # если х есть, берем коэффициент или 1
                if list1[i].index('x') > 0:
                    a = int(list1[i][:list1[i].index('x')])
                else: a = 1
                i += 1
            else: a = 0 # если х нет - коэффициент обнуляем
            i += 1
            if 'x' in list2[j]: # то же для второго списка
                if list2[j].index('x') > 0:
                    b = int(list2[j][:list2[j].index('x')])
                else: b = 1
                j += 1
            else: b = 0
            j += 1
            
            member = a + b
            result = result + str(member) + 'x + '

    # складываем последние коэффициенты они же последние элементы списков
    if 'x' not in list1[-1]: a = int(list1[-1])
    else: a = 0
    if 'x' not in list2[-1]: b = int(list2[-1])
    else: b = 0
    if a == 0 and b == 0: result = result[:-3] + ' = 0'
    else: result = result + str(a + b) + ' = 0' 

    return result


data = open('file.txt', 'r') # Беру оба уравнения из одного файла.
polynom = data.read() + ' '
data.close

polyList = polynom.split('\n')

polynom1 = polyList[0]
polynom2 = polyList[1]

print('Уравнения из файла:')
print(polynom1)
print(polynom2)

polynom1 = polynom1[:polynom1.index('=')-1] # отрезаем " = 0"
polynom2 = polynom2[:polynom2.index('=')-1]

# вырезаем "+ "
element = 0
while element < len(polynom1):
    if polynom1[element] == '+': polynom1 = polynom1[:element - 1] + polynom1[element + 1:]
    element += 1
element = 0
while element < len(polynom2):
    if polynom2[element] == '+': polynom2 = polynom2[:element - 1] + polynom2[element + 1:]
    element += 1

polynom1 = polynom1.split(' ') # разбиваем строку и получаем список
polynom2 = polynom2.split(' ')

print('Сумма многочленов:')
print(PolySum(polynom1, polynom2))

file = open('file1.txt', 'w')
file.write(PolySum(polynom1, polynom2))
file.close