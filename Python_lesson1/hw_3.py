# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

numbers = list(range(1, 101))
# print(numbers)
for i in numbers:
    if i == 1:
        print(i, 'процент')
    if i < 5 and i != 1:
        print(i, 'процента')
    if i < 20 and i > 4:
        print(i, 'процентов')
    if i > 20 and i % 10 <= 4 and i % 10 > 1 :
        print(i, 'процента')
    if i >= 20 and i % 10 ==1:
        print(i, 'процент')
    if i > 20 and i % 10 > 4 and i % 10 <= 9:
        print(i, 'процентов')
    if i >= 20 and i % 10 == 0:
        print(i, 'процентов')