# 8.	Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

from random import randint


def Gamefield (array): # Отрисовка игрового поля
    print('―――――――――――――')
    for i in range(3):
        print('|', end='')
        for j in range(3):
            print(f" {array[i][j]}", end=' |')
        print('\n―――――――――――――')

def WinTest (array): # Проверка на выигрыш
    for i in range(3): # Проверяем строки
        player = bot = 0
        for j in range(3):
            if array[i][j] == "X": player += 1
            if array[i][j] == "O": bot += 1
        if player == 3: 
            print('Вы победили.')
            quit()
        if bot == 3: 
            print('Бот победил вас!')
            quit()
    for i in range(3): # Проверяем столбцы
        player = bot = 0
        for j in range(3):
            if array[j][i] == "X": player += 1
            if array[j][i] == "O": bot += 1
        if player == 3: 
            print('Вы победили.')
            quit()
        if bot == 3: 
            print('Бот победил вас!')
            quit()
    player = bot = 0
    for i in range(3): # Проверяем первую диагональ
        if array[i][i] == "X": player += 1
        if array[i][i] == "O": bot += 1
        if player == 3: 
            print('Вы победили.')
            quit()
        if bot == 3: 
            print('Бот победил вас!')
            quit()
    player = bot = 0
    for i in range(3): # Проверяем вторую диагональ
        if array[i][2-i] == "X": player += 1
        if array[i][2-i] == "O": bot += 1
        if player == 3: 
            print('Вы победили.')
            quit()
        if bot == 3: 
            print('Бот победил вас!')
            quit()
    
def PlayerMove (array): # Ход игрока
    flag = 0
    while flag == 0:
        a = int(input('В какое поле желаете поставить Х? '))
        if a >= 1 and a <= 9:
            coorX = int(a/3.5)
            coorY = ((a-1)%3)
            if array[coorX][coorY] == "X" or array[coorX][coorY] == "O": 
                print("Это поле занято")
            else: 
                array [coorX][coorY] = "X"
                flag = 1
        else: print('Поля от 1 до 9')

def BotMove (array): # Ход бота
    flag = 0
    while flag == 0:
        b = randint(1, 9)
        coorX = int(b/3.5)
        coorY = ((b-1)%3)
        if array[coorX][coorY] != "X" and array[coorX][coorY] != "O": 
            array [coorX][coorY] = "O"
            flag = 1
            print(f'А бот занял поле {b}')



arr = [[1,2,3],[4,5,6],[7,8,9]]
Gamefield(arr)

for i in range(4):
    PlayerMove(arr)
    WinTest(arr)
    BotMove(arr)
    Gamefield(arr)
    WinTest(arr)
PlayerMove(arr)
Gamefield(arr)
WinTest(arr)
print('Ничья')
