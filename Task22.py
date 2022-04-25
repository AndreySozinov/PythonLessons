# Определить, присутствует ли в заданном списке строк, некоторое число

list = ['adc21', 'i4op0', '33uio']

number = 45

for string in list:
    if str(number) in string:
        print('Присутствует')
        quit()
print("Отсутствует")