a = []
b = []
c = []

for _ in range(10):
    a.append(int(input('Digite um inteiro para adicionar na lista A: ')))
    b.append(int(input('Digite um inteiro para adicionar na lista B: ')))

for i in range(10):
    c.append(a[i] - b[i])

print(f'\nVetor A: {a}\n'
      f'Vetor B: {b}\n'
      f'Vetor C: {c}')
