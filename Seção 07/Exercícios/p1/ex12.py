vetor = list()

for _ in range(5):
    vetor.append(int(input('Digite um número inteiro: ')))

print(f'\nTodos os valores lidos: {vetor}\n'
      f'Maior valor: {max(vetor)}\n'
      f'Menor valor: {min(vetor)}\n'
      f'Média dos valores: {(sum(vetor) / len(vetor)):.1f}')
