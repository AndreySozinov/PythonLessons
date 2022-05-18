# 8.	Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

from random import randint


def Gamefield (array): # Рисуем игровое поле
    print('―――――――――――――')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(f" {array[i][j]}", end=' |')
        print('\n―――――――――――――')

def WinTest (array): # Проверяем на выигрыш
    for i in range(3): # Проверяем строки
        player = bot = 0
        for j in range(3):
            if array[i][j] == "X": player += 1
            if array[i][j] == "O": bot += 1
        if player == 3: print('Вы победили.')
        if bot == 3: print('Бот победил вас!')
        break
    for i in range(3): # Проверяем столбцы
        player = bot = 0
        for j in range(3):
            if array[j][i] == "X": player += 1
            if array[j][i] == "O": bot += 1
        if player == 3: print('Вы победили.')
        if bot == 3: print('Бот победил вас!')
        break
    player = bot = 0
    for i in range(3): # Проверяем первую диагональ
        if array[i][i] == "X": player += 1
        if array[i][i] == "O": bot += 1
        if player == 3: print('Вы победили.')
        if bot == 3: print('Бот победил вас!')
        break
    player = bot = 0
    for i in range(3): # Проверяем вторую диагональ
        if array[2-i][2-i] == "X": player += 1
        if array[2-i][2-i] == "O": bot += 1
        if player == 3: print('Вы победили.')
        if bot == 3: print('Бот победил вас!')
        break
    
def PlayerMove (array): # Ход игрока
    a = int(input('В какое поле желаете поставить Х?'))
    coorX = int(a/4)
    coorY = (a%4)-1
    if array[coorX][coorY] == "X" or array[coorX][coorY] == "O": print("Это поле занято")
    else: array [coorX][coorY] = "X"

def BotMove (array): # Ход бота
    flag = 0
    while flag == 0:
        b = randint(1, 9)
        coorX = int(b/4)
        coorY = (b%4)-1
        if array[coorX][coorY] != "X" and array[coorX][coorY] != "O": 
            array [coorX][coorY] = "O"
            flag = 1



arr = [[1,2,3],[4,5,6],[7,8,9]]
Gamefield(arr)
WinTest(arr)
