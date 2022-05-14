# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

def PolySum(list1, list2):
    result = ""
    if len(list1) > len(list2): length = len(list1)
    else: length = len(list2)
    i = 0
    j = 0
    while i < length-1 and j < length-1:
        if ('x' in list1[i] or 'x' in list2[j]) and list1[i][-1] != 'x' and list2[j][-1] != 'x':
            if list1[i][list1[i].index('^'):] == list2[j][list2[j].index('^'):]: 
                member = int(list1[i][:list1[i].index('x')]) + int(list2[j][:list2[j].index('x')])
                result = result + str(member) + list1[i][list1[i].index('x'):] + ' + '
                i += 1
                j += 1
            elif list1[i][list1[i].index('^'):] > list2[j][list2[j].index('^'):]:
                result = result + list1[i] + ' + '
                i += 1
            else: 
                result = result + list2[i] + ' + '
                j += 1
        else: 
            member = int(list1[i][:list1[i].index('x')]) + int(list2[j][:list2[j].index('x')])
            i += 1
            j += 1
            result = result + str(member) + 'x + '
            result = result + str(int(list1[-1]) + int(list2[-1])) + ' = 0' 

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