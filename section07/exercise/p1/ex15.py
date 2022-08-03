from collections import defaultdict

vetor = list()
d = defaultdict(int)
lista = list()

for _ in range(20):
    vetor.append(int(input('Digite um número inteiro: ')))

for chave in vetor:
    d[chave] += 1

for chave, valor in d.items():
    if valor == 1:
        lista.append(chave)

print(f'\nVetor: {vetor}\n'
      f'Elementos não repetidos no vetor: {lista}')
