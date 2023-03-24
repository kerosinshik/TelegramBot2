items = [
    {
    "name": "Кроссовки",
    "price": "7540.5",
    "currency": "rub"
    },
    {
    "name": "Шорты",
    "price": "1313.2",
    "currency": "rub"
    },
    {
    "name": "Кепка",
    "price": "738.0",
    "currency": "rub"
    },
    {
    "name": "Чемодан",
    "price": "2300.85",
    "currency": "rub"
    },
]

min_price = float(items[0]['price'])
print(min_price)

for i in items:
    if float(i["price"]) < min_price:
        min_price = float(i["price"])
print(min_price)


