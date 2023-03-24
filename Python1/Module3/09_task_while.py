n = int(input('n: '))

div = 1
total = 0

while div < n:
    if n % div == 0:
        total += div
    div +=1

if total == n:
    print('ДА')
else:
    print('НЕТ')