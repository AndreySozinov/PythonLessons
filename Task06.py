# 6.	Дано число обозначающее день недели. Вывести его название 
# и указать является ли он выходным.

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']
day_number = int(input('Введите номер дня недели\n'))
print(week[day_number - 1])
if day_number > 5: print('Это выходной день')