a = []
b = []
c = []

for _ in range(10):
    a.append(int(input('Digite um inteiro A: ')))
    b.append(int(input('Digite um inteiro B: ')))

for i in range(10):
    if i % 2 == 0:
        c.append(a[i])
    else:
        c.append(b[i])

print(f'\nA = {a}\n'
      f'B = {b}\n'
      f'C = {c}')
