# 16. Найти корни квадратного уравнения Ax² + Bx + C = 0

def squareEquation(a, b, c):
    if a == 0: 
        print('Это не квадратное уравнение')
        quit()
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print('Уравнение не имеет корней')
        quit()
    elif discriminant == 0:
        print(f'Оба корня равны {(-b) / (2 * a)}')
        quit()
    x1 = round(((-b) - discriminant ** .5) / (2 * a), 3)
    x2 = round(((-b) + discriminant ** .5) / (2 * a), 3)
    print(f'x1 = {x1}; x2 = {x2}')

squareEquation(1, 2, 1)