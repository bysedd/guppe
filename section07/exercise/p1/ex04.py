vetor = [int(input('Digite um número inteiro: ')) for _ in range(8)]

x = int(input('\nX entre 0-7: '))
y = int(input('Y entre 0-7: '))

soma = vetor[x] + vetor[y]

print(f'\nSoma dos valores encontrados nas respectivas posições {x} e {y}: {soma}')
