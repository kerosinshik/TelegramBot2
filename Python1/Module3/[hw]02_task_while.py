n = int(input('n: '))

i = 1
total = 0

while i < n:
    card_number = int(input('Номер карточки: '))
    total += card_number
    i += 1

sum_n = (i + n) * n / 2

print('Номер потерянной карточки:', int(sum_n - total))
