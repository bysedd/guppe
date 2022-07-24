x = set()
y = set()
soma = 0
produto = 1

for _ in range(5):
    x.add(int(input('Digite um inteiro para o conjunto X (sem repetir): ')))
print()
for _ in range(5):
    y.add(int(input('Digite um inteiro para o conjunto Y (sem repetir): ')))

print(f'\nConjunto X: {x}\n'
      f'Conjunto Y: {y}\n')

for elemento in x:
    soma += elemento
    produto *= elemento
for elemento in y:
    soma += elemento
    produto *= elemento

print(f'Soma entre X e Y: {soma}\n'
      f'Produto entre X e Y: {produto}\n'
      f'Diferença entre X e Y: {x.difference(y)}\n'
      f'Interseção entre X e Y: {x.intersection(y)}\n'
      f'União entre X e Y: {x.union(y)}\n'
      f'Diferença entre Y e X: {y.difference(x)}')
