def even(n):
    return n % 2 == 0

n = float(input('Введите число: '))
if even(n):
   print("Число четное")
else:
   print("Число не четное")