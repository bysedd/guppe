vetor = list()

for _ in range(10):
    vetor.append(int(input('Digite um número inteiro: ')))

print(f'{vetor}\n'
      f'Maior elemento: {max(vetor)}, posição em que ele se encontra: {vetor.index(max(vetor)) + 1}')
