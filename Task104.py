# 4. В файле находится N натуральных чисел, записанных через пробел. 
#    Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

file = open('file.txt', 'r')
data = file.read()
file.close

numbers = (data.split(' '))
print(numbers)

for i in range(1, len(numbers)):
    if int(numbers[i]) - 1 != int(numbers[i - 1]): print(f'Не хватает числа {int(numbers[i]) - 1}')
# В задании требуется только найти недостающее число, поэтому стоп.