# 13. Пользователь задаёт две строки. Определить количество вхождений 
# одной строки в другой

string_one = "Привет мир, привет страна!"
string_two = "привет"
sum = 0

string_one = string_one.lower() # делаем все буквы маленькими
string_two = string_two.lower()

for i in range(0, len(string_one) - len(string_two) + 1):
    if string_one[i:i+len(string_two)] == string_two:
        sum += 1

print(sum)