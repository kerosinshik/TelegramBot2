text = input('Введите текст: ')

point_sum = text.count('.')
comma_sum = text.count(',')

if point_sum > comma_sum:
    print('Точек больше.')
elif comma_sum > point_sum:
    print('Запятых больше.')
else:
    print('Одинаково.')
