a = int(input('a: '))
b = int(input('b: '))

n = a
while n <= b:
    if n % 2 == 0:
        print(n)
    n += 1