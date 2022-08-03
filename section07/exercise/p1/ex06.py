vetor = list()

for _ in range(10):
    vetor.append(int(input('Digite um número inteiro: ')))

print(f'\n{vetor}\n'
      f'Maior elemento: {max(vetor)}\n'
      f'Menor elemento: {min(vetor)}')
