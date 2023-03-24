cost = float(input('Цена: '))
n = int(input('Количество: '))

i = 1

while i < n:
    print(i, cost * i, 'рублей')
    i += 1
