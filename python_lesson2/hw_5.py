# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
# остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price = [1, 2.3, 4.41, 6, 4, 91.2, 121, 111, 11.99, 45.99, 542.1, 1231.09, 54]
print(id(price)) # доказал что после сортировки объект остался тот же

for el in price:                              #
    rub, kop = f'{el:.2f}'.split('.')         # вывел цены через запятую и отоброзил в виде <rub> руб <kop> коп
    print(f'{rub} руб {kop} коп', end = ', ') #

price.sort()
print(id(price))# доказал что после сортировки объект остался тот же
new_list = sorted(price, reverse= True) # новый список отсортированный по убыванию
print(new_list)
new_list.sort()             #
print(f'{new_list[-5:]}')   #вывел цену 5 самых дорогих товаров по возрастанию

