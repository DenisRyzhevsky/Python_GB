# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
# если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?(

def thesaurus(*names):
    var = {}
    for el in sorted(list(names)):
        var.setdefault(el[0], []).append(el)
    print(var)
thesaurus("Иван", "Мария", "Петр", "Илья")
