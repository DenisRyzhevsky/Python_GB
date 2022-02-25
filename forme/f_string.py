import datetime
result = 14217482137524
number = 21.9302
print(f'{number:.02f}') # оставили после точки 2 символа
print(f'{number:012}') # заполняет нулями пока не будет 12 символов
print(f'{number:=^12}') # ставит в середину
print(f'{number:0>12}') #вправо
print(f'{number:0<12}')#влево
print(f'{result:,}') # ставим разеделитель запятую 14,217,482,137,524
today = datetime.datetime.now()
print(f'{today:%d-%m-%Y  %H:%M}')
a = 12
b = 100
print(f'{a/b:%}') # ищем проценты если поставить точку 02f оставим только 2символа после точки
