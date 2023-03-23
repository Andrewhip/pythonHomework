num = int(input('Введите количество элементов в массиве '))
mass = []
for i in range(1, num+1):
    nums_mass = int(input(f'Введите {i} число '))
    mass.append(nums_mass)
elem = int(input())
closest = mass[0]
for i in range(1, num):
    diff = mass[i] - elem
    if diff < 0:
        diff = -diff
    if diff < abs(closest - elem ):
        closest = mass[i]
print(closest)
