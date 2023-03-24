level = int(input('Количество уровней: '))

total = 0
product = 0

while level > 0:
    product = level ** 2
    total += product
    level -= 1
print(total)