m = int(input('Введите m: '))
n = int(input('Введите n: '))
k = int(input('Введите k: '))

if k < m * n:
    if k % m == 0 or k % n == 0:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')