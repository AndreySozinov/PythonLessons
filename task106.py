string = 'Напишите абвегедейка программу, абвегедейка удаляющую из текста все слова содержащие "абв" абвегедейка'

text = list(filter(lambda x: 'абв' not in x, string.split()))
result = " ".join(text)
print(f'Исходный текст:\n {string}')
print(f'Преобразованный текст:\n {result}')
