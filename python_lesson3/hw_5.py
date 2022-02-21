# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choice, randrange
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(el, unique = False):
    """

    Функция возвращает случайные шутки, собранные из 3 списоков слов
    unique - уникальные шутки True, False - не уникальные

    """
    nou, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    list_min = min(nou, adv, adj)

    while el and len(list_min):
        num = randrange(len(list_min))
        if unique:
            jokes.append(f"{nou.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        el -= 1
    return jokes

print(get_jokes(10))




