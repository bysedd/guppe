vetor = []
lista = []

for _ in range(10):
    vetor.append(int(input('Digite um número inteiro: ')))

x = int(input('\nx = '))

for numeros in vetor:
    if numeros % x == 0:
        lista.append(numeros)

print(f'\nMúltiplos de {x} num vetor {vetor} = {lista}\n')
