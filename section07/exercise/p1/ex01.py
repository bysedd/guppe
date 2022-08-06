# noinspection PyListCreation
a = [1, 2, 3, 4, 5, 6]
print(a)

# (a)
for numero in [1, 0, 5, -2, -5, 7]:
    a.append(numero)
print(a)

# (b)
print(a[0] + a[1] + a[5])

# (c)
a[4] = 100

# (d)
print([valor for valor in a])
