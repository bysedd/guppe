c1 = set()
c2 = set()

for _ in range(10):
    c1.add(int(input('Digite um inteiro para o Conjunto 1: ')))
print()
for _ in range(10):
    c2.add(int(input('Digite um inteiro para o Conjunto 2: ')))

c3 = c1.intersection(c2)

print(f'\nPrimeiro conjunto: {c1}\n'
      f'Segundo conjunto: {c2}\n'
      f'Terceiro conjunto: {c3}')
