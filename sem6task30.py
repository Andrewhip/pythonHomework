'''Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

def a_n(a,n,d):
    list1 =[]
    for i in range(n+1):
        an = a + (i - 1) * d
        list1.append(an)
    return list1

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(a_n(num1, num3, num2))

