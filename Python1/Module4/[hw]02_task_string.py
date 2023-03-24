text = input('Введите текст: ')

words = text.split()
word_b = ''

for i in words:
    if i[0] == 'б':
        word_b = i
        print(word_b)
        break
if word_b == '':
    print('Слова нет')