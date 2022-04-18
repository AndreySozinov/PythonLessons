# 15. Дано количество секунд. Вывести результат в виде: 
# дни:часы:минуты:секунды

seconds = int(input('Введите количество секунд\n'))
days = int(seconds / 86400)
seconds = seconds % 86400
hours = int(seconds / 3600)
seconds = seconds % 3600
minutes = int(seconds / 60)
seconds = seconds % 60
print(f'дни: {days}, часы: {hours}, минуты: {minutes}, секунды: {seconds}')