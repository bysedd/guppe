vetor = list()

for _ in range(8):
    vetor.append(int(input('Digite um número inteiro: ')))

x = int(input('\nX entre 0-7: '))
y = int(input('Y entre 0-7: '))

soma = vetor[x] + vetor[y]

print(f'\nSoma dos valores encontrados nas respectivas posições {x} e {y}: {soma}')
