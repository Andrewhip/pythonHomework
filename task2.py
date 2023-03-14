#Задача 2: Найдите сумму цифр трехзначного числа.

# num = int(input())
# total = 0
# while num!=0:
#     y = num%10
#     total += y
#     num = num//10
# print(total)

#можно сделать через строки
num = int(input())
num = str(num)
count = 0
for i in range(len((num))):
    count += int(num[i])
print(count)
