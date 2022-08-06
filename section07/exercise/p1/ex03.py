from math import sqrt

p = '{'
c1 = {float(input('Digite um número real: ')) for _ in range(10)}
c2 = {sqrt(elemento) for elemento in c1}

print(f'\n{c1:.1f}')
print('Raiz quadrada dos números digitados acima, aproximadamente:')

for elemento in c2:
    p += f'{elemento:.1f}, '
p = p[:len(p) - 2] + '}'

print(p)
