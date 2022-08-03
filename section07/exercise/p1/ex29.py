lista = list()

while True:
    lista.append(int(input()))
    if lista.count(0):
        lista.pop()
        break

p = ''
qtd = list()
s = 0
print('\nNúmeros pares digitados: [', end='')
for elemento in lista:
    if elemento % 2 == 0:
        qtd.append(elemento)
        s += elemento
        p += f'{elemento}, '
print(p[:len(p) - 2] + ']')
print(f'Quantidade de números pares digitados: {len(qtd)}')
print(f'Soma dos números pares digitados: {s}')

p = ''
qtd = list()
s = 0
print('\nNúmeros ímpares digitados: [', end='')
for elemento in lista:
    if elemento % 2 != 0:
        qtd.append(elemento)
        s += elemento
        p += f'{elemento}, '
print(p[:len(p) - 2] + ']')
print(f'Quantidade de números ímpares digitados: {len(qtd)}')
print(f'Soma dos números ímpares digitados: {s}')
