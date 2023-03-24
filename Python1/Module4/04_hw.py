import random

n = int(input('Введите количество элементов: '))

BEGINNING = -100
FINISH = 100
numbers = []
i = 1

while i <= n:
    numbers.append(random.randint(BEGINNING, FINISH))
    i += 1
print('Список произвольных элементов:')
print(numbers)

results = []

for j in numbers:
    if j > 0 and (j ** 0.5) % 1 == 0:
        results.append(int(j ** 0.5))
print()
print('Результат: ', results)
