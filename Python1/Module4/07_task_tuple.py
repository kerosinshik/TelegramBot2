tup = (2, 4, 6, -4, 12, 0, 5)

max_number = tup[0]

print(max_number)

i = 0

while i < len(tup):
#for number in tup:
#    print(i)
    if tup[i] > tup[i + 1]:
        max_number = tup[i]
    else:
        max_number = tup[i + 1]
    i += 1
print(max_number)
