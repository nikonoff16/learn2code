x = [2, 3, 4, 5, 6]
y = [i * i for i in x if i % 2 == 0]
print(y)

z = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(z)

# z = []
# for x in range(3):
#     for y in range(3):
#         if y >=x:
#             z.append((x, y))
print(next(z))
print(next(z))
