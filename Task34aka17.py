# 17. Найти НОК двух чисел

def lcm(m, n):
    result = max(m, n)
    while result % m != 0 or result % n != 0:
        result += 1
    print(f'HOK = {result}')

lcm(16, 20)