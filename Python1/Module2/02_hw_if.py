n = int(input('Введите количество: '))

n = n % 100
if n % 10 == 1 and n != 11:
    print('корова')
elif 2 <= n % 10 <= 4 and not 12 <= n <= 14:
    print('коровы')
else:
    print('коров')
