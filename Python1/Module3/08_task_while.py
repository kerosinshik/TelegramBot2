n = int(input('n: '))

i = 2

while i < n:
    if n % i == 0:
        print(i)
    i += 1
    else:
        print('Число простое')
