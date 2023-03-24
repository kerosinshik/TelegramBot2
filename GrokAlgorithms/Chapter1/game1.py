import random

comp_num = 0
comp_symbol = 0
winner = 0
user_symbol = 0

# comp_num = random.randint(1, 3)
# print(comp_num)

while winner == 0 or winner == 'Ничья':
    print('Введите "1", если хотите показать "камень".')
    print('Введите "2", если хотите показать "ножницы".')
    print('Введите "3", если хотите показать "бумага".')

    user_num = int(input('Ваше число: '))
    if user_num == 1:
        user_symbol = 'камень'
    elif user_num == 2:
        user_symbol = 'ножницы'
    else:
        user_symbol = 'бумага'
    print("Вы показали:", user_symbol)

    comp_num = random.randint(1, 3)
    print(comp_num)
    if comp_num == 1:
        comp_symbol = 'камень'
    elif comp_num == 2:
        comp_symbol = 'ножницы'
    else:
        comp_symbol = 'бумага'
print("Компьютер показал:", comp_symbol)
#
if comp_symbol == 'камень' and user_symbol == 'ножницы':
    winner = 'Компьютер'
elif comp_symbol == 'камень' and user_symbol == 'бумага':
    winner = 'Вы'
elif comp_symbol == 'ножницы' and user_symbol == 'камень':
    winner = 'Вы'
elif comp_symbol == 'ножницы' and user_symbol == 'бумага':
    winner = 'Компьютер'
elif comp_symbol == 'бумага' and user_symbol == 'камень':
    winner = 'Компьютер'
elif comp_symbol == 'бумага' and user_symbol == 'ножницы':
    winner = 'Вы'
elif comp_symbol == user_symbol:
    winner = 'Ничья'
print(winner)
