num = int(input('Введите колличество элементов в массиве '))
mass = []
count = 0
for i in range(1,num+1):
        nums_mass = int(input(f'Введите {i} число '))
        mass.append(nums_mass)
x = int(input('Введите число для проверки: '))
for i in range(len(mass)):
        if x == mass[i]:
                count+=1
print(count)