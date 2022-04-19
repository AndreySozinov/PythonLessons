# 16. Написать программу проверки, является ли строка палиндромом

palindrom = "а роза упала н алапу азор а"

for i in range(0, int(len(palindrom) / 2)):
    if palindrom[i] != palindrom[- 1 - i]:
        print('Это не палиндром')
        quit()
print('Это палиндром')