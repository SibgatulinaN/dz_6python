# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# n = int(input('Введите первый элемент: '))
# s = int(input('Введите разность : '))
# q = int(input('Введите количесто элементов: '))


def arithmetic_progression(n, s, q):
    arr = [n]
    for i in range(1,q):
        arr.append(arr[i-1] + s)
    return arr
print(arithmetic_progression(n, s, q))    

a1 = 3
d = 2
n = 10
for i in range(n):
    print(a1 + i * d, end=' ')