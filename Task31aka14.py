# 14. Дано число. Составить список чисел Фибоначчи, в том числе для 
# отрицательных индексов. Т е для k = 8, список будет выглядеть так: 
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def FibonacciAndNeg(k):
    fibonacci = [0, 1]
    if k > 1:
        for i in list(range(1, k)): # Просто ряд Фибоначчи
            fibonacci.append(fibonacci[i] + fibonacci[i - 1])
    negfibonacci = []
    if k == 1:
        negfibonacci = [1]
    else:
        for i in list(range(1, k + 1)): # Негфибоначчи по тождеству к Фибоначчи
            negfibonacci.append((-1)**(i) * fibonacci[-i]) # Спасибо Википедии
    result = negfibonacci + fibonacci # Объединение Фибоначчи и Негфибоначчи
    print(result)

FibonacciAndNeg(8)