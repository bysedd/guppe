pares = []
c = 0

vetor = [int(input('Digite um número inteiro: ')) for _ in range(10)]

for elemento in vetor:
    if elemento % 2 == 0:
        c += 1
        pares.append(elemento)

print(f'\nO vetor {vetor} possui {c} números pares, sendo eles: {pares}')
