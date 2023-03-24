import random

n = int(input('Введите количество элементов: '))
BEGINNING = -100
FINISH = 100
numbers = []
i = 1

while i <= n:
    numbers.append(random.randint(BEGINNING, FINISH))
    i += 1
print(numbers)
