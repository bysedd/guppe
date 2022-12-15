from collections import defaultdict

vetor = []
d = defaultdict(int)
lista = []

for _ in range(10):
    vetor.append(input('Digite qualquer coisa: '))

for chave in vetor:
    d[chave] += 1

for chave, valor in d.items():
    if valor > 1:
        lista.append(chave)

print(f'\nVetor: {vetor}\n'
      f'Valores iguais: {lista}')
