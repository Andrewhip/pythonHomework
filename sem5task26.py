'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

def exponentiate(a,b):
    if a==0 and b==0:
        return 0
    if b == 1:
        return a
    else:
        return a * exponentiate(a,b-1)

a= int(input())
b= int(input())
print(exponentiate(a,b))