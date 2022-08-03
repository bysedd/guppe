x = int(input('x: '))
y = int(input('y: '))
soma, mult = 0, 1
if x > y:
    for c in range(y, x + 1):
        if c % 2 == 0:
            soma += c
        else:
            mult *= c
elif x < y:
    for c in range(x, y + 1):
        if c % 2 == 0:
            soma += c
        else:
            mult *= c
print(f'\n\033[0:34m{x} --- {y}\033[m')
print(f'Soma total: \033[1:32m{soma}\033[m')
print(f'Multiplicação total: \033[1:33m{mult}\033[m')
