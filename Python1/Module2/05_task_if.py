n = int(input('Введите число:'))

if n % 3 == 0 and n % 5 == 0:
    print('Foobar')
elif n % 3 == 0:
    print('Foo')
elif n % 5 == 0:
    print('Bar')
else:
    print('')
