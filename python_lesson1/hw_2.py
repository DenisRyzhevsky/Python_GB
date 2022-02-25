# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

my_list = list(range(1, 1001, 2))
cube_list = []
cube_result = 0
cube_result_2 = 0

for el in my_list:
    cube_list.append(el ** 3)

for el in cube_list:
    el_1 = el
    cube_sum = 0

    while el != 0:
        cube_sum += el % 10
        el = el // 10
    if cube_sum % 7 == 0:
        cube_result += el_1

for i in range(len(cube_list)):
    cube_list[i] += 17
for ele in cube_list:
    cube_sum_2 = 0
    ele_1 = ele
    while ele:
        cube_sum_2 += ele % 10
        ele = ele // 10
    if cube_sum_2 % 7 == 0:
        cube_result_2 += ele_1

print(cube_result)
print(cube_result_2)
