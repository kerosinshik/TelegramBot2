names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_length = 1

for i in names:

    if len(i) > max_length:
        max_length = len(i)
        print(i)
print(max_length)
