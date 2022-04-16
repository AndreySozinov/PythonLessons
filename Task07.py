# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
#    всех значений предикат

predicats = [False, True]

print('X      Y      Z      Проверка истинности')
for x in predicats:
    for y in predicats:
        for z in predicats:
            answer = not(x or y or z) is (not x and not y and not z)
            print(x, y, z, '         ', answer)