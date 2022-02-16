# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# 	Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

duration = int(input('Введите кол-во секунд: '))
sec = duration % 60
min = duration / 60
hour = duration / 60 / 60
day = duration / duration

if duration < 60:
    print(sec, 'сек')
elif duration >= 60 and duration < 3600:
    print(int(min), 'мин', sec, 'сек')
elif duration >= 3600 and duration < 86400:
    print(int(hour), 'час', int(min) % 60, 'мин', sec, 'сек')
elif duration >= 86400:
    print(int(day), 'дн', int(hour) % 24, 'час', int(min) % 60, 'мин', sec, 'сек')

