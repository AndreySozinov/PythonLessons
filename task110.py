# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

def Rls(string):
    count = 1
    res = ""
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else: 
            res = res + str(count) + string[i]
            count = 1
    return res + str(count) + string[i]



print(Rls("AAAAAAAABCCCDD"))