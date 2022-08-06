vetor = [int(input('Digite um número inteiro: ')) for _ in range(10)]

print(f'\n{vetor}\n'
      f'Maior elemento: {max(vetor)}, posição em que ele se encontra: {vetor.index(max(vetor)) + 1}')
