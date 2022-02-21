# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

translate = {"zero": "ноль", "two": "два", "three": "три",
                "four": "чертыре", "five": "пять", "sex": "шесть",
                "seven": "семь", "eight": "восемь", "nine": "девять",
                "ten": "десять", "one": "один"}

def num_translate(number):
    if number.istitle():
        return print(str(translate.get(number.lower())).title())
    return print(translate.get(number))

num_translate('Two') # переводит числительные
num_translate('ONE')  #возвращает None