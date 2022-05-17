# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

def RlsCompression(string):
    count = 1
    res = ""
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else: 
            res = res + str(count) + string[i]
            count = 1
    return res + str(count) + string[i]

def RlsDecompression(string):
    res = ""
    for i in range(0, len(string)-1, 2):
        for j in range(int(string[i])):
            res = res + string[i+1]
    return res


file = open('rlsdecompress.txt', 'r')
rawdata = file.read()
file.close

compress = RlsCompression(rawdata)

file = open('rlscompress.txt', 'w')
file.write(compress)
file.close

file = open('rlscompress.txt', 'r')
data = file.read()
file.close

decompress = RlsDecompression(data)

file = open('rlsdecompress.txt', 'w')
file.write(decompress)
file.close