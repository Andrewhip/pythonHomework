n = int(input("Введите колличество монет: "))
zero_coins = 0
one_coins = 0
for i in range(n):
    coin = int(input('Введите 0 или 1: '))
    if coin ==0:
        zero_coins+=1
    else:
        one_coins += 1
if zero_coins<one_coins:
    print("Перевернуть нужно", zero_coins, 'монет')
else:
    print("Перевернуть нужно", one_coins, 'монет')

