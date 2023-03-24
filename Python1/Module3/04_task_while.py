n = int(input('n: '))

count = 0
i = 0

while i < n:
    number = int(input('Введите число: '))
    if number > 0:
        count += 1
    i += 1
print('Число положительных чисел', count)
