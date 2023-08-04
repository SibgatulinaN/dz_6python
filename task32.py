# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random
n = int(input('Введите количество элементов в списке: '))
first_list = list()
for _ in range(n):
    number = random.randint(1, 10)
    first_list.append(number)
print(first_list) 

def diapason(first_list, min, max):
    res = []
    for i in range(len(first_list)):
        if max >= first_list[i] >= min:
            res.append(i)
    return res

print(diapason (first_list,5,14))
