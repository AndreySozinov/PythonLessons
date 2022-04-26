# 7. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

st = set()

for i in range(100):
    st.add(str(i))

for i in st:
    print(int(i))
    break

# import keyboard

# number = 0
# print("Нажмите пробел\n")

# while True:
#     try:
#         for i in range(0, 100):
#             number = i
#             if keyboard.is_pressed('0'):
#                 break
#         for i in range(100, 0, -1):
#             number = i
#             if keyboard.is_pressed('0'):
#                 break
#     except:
#         break
# print(number) 