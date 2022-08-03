vetor = list()
pares = list()
c = 0

for _ in range(10):
    vetor.append(int(input('Digite um número inteiro: ')))

for elemento in vetor:
    if elemento % 2 == 0:
        c += 1
        pares.append(elemento)

print(f'O vetor {vetor} possui {c} números pares, sendo eles: {pares}')
