n = int(input('n: '))

total = 0
i = 0

while i < n:
    if i % 2 == 0:
        total += i
    i += 1
print('Сумма четных чисел от 0 до', n, '=', total)
