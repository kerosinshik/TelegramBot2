budget = int(input('Денег у покупателя: '))
cost = int(input('Цена товара: '))

if budget >= cost:
    print('Осталось денег:', budget - cost, 'рублей.')
else:
    print('Денег недостаточно.')
