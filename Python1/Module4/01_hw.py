names = ["Иван", "Вячеслав", "Василий", "Петр"]

i = 0

while i < len(names):
    print(str(names[i]), end='')
    i += 1
    if i == len(names):
        print('.')
        break
    print(', ', end='')

