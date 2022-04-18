from itertools import count
string_one = "Привет мир, привет страна!"
string_two = "привет"

sum = count(string_two.islower() in string_one.islower())
print(sum)