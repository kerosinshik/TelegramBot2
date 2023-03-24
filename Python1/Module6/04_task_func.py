# def can_triangle(p1, p2, p3):
#     x1 = int(input())
#     y1 = int(input())
#     x2 = int(input())
#     y2 = int(input())
#     x3 = int(input())
#     y3 = int(input())
#
#     p1 = (x1, y1)
#     p2 = (x2, y2)
#     p3 = (x3, y3)
#
#     return p1

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)

a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

print(p1)

# Пример вызова функции
# a = can_triangle((10, 12), (14, 18), (12, 12))
#
# print(a)