def max4(n1, n2, n3, n4):
    numbers = [n1, n2, n3, n4]
    max_val = numbers[0]
    for i in numbers:
        if i >= max_val:
            max_val = i
    return max_val

print(max4)

# Тестируем функцию
print(max4(5, 6, 12, 7))
print(max4(-10, -12, -4, -9))
print(max4(2.5, 2.6, 2.6, 2.4))
print(max4(-2.5, 0, -1.2, -0.4))
print(max4(-2, -2, -2, -2))