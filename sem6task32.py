'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]'''
list1 = input().split()
list2 = []
min_num = int(input())
max_num = int(input())
for i in range(len(list1)):
    if min_num<=int(list1[i])<=max_num:
        list2.append(i)
print(list2)