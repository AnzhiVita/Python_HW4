# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)

import random
a, b, s = 1, 10, 20
list_1=list(map(lambda _: random.randint(a, b), range(s)))
print(list_1)

list_2 = []
min = int(input('Введите min: '))
max = int(input('Введите max: '))
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)