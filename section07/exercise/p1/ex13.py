vetor = list()

for _ in range(5):
    vetor.append(int(input('Digite um número inteiro: ')))

print(f'\nVetor: {vetor}\n'
      f'Posição do maior valor lido: {vetor.index(max(vetor))}\n'
      f'Posição do menor valor lido: {vetor.index(min(vetor))}')
