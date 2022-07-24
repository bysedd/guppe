# noinspection PyListCreation
a = [1, 2, 3, 4, 5, 6]

# (a)
lista = [1, 0, 5, -2, -5, 7]
for numero in lista:
    a.append(numero)

# (b)
s = a[0] + a[1] + a[5]

# (c)
a[4] = 100

# (d)
for valor in a:
    print(valor, end=' ')
