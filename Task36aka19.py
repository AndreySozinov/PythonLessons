# 19. Составить список простых множителей натурального числа N

def simplemulti(n):
    list = []
    resultlist = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
    for number in list:
        count = 0
        for i in range(2, number):
            if number % i == 0: count += 1
        if count == 0: resultlist.append(number)
    print(resultlist)

simplemulti(87)