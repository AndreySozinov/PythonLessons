# 9.	Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

quarter_number = int(input('Введите номер четверти системы координат\n'))

if quarter_number == 1: print('X > 0; Y > 0')
elif quarter_number == 2: print('X < 0; Y > 0')
elif quarter_number == 3: print('X < 0; Y < 0')
elif quarter_number == 4: print('X > 0; Y < 0')
else: print('Нет такой четверти')