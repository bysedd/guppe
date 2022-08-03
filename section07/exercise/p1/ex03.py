from math import sqrt

c1 = set()
c2 = set()
p = '{'

for _ in range(10):
    c1.add(float(input('Digite um número real: ')))

for elemento in c1:
    c2.add(sqrt(elemento))

print(f'\n{c1}')
print('Raiz quadrada dos números digitados acima, aproximadamente')

for elemento in c2:
    p += f'{elemento:.1f}, '
p = p[:len(p) - 2] + '}'

print(p)
