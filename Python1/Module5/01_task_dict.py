# Информация о товаре
item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub"}
# Количество товаров
item_count = 8
# Курс доллара
dollar_rate = 74.12

cost = float(item['price']) * item_count / dollar_rate

print(f'Стоимость покупки: {cost:.2f} долларов.')