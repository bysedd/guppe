vetor = []

for _ in range(15):
    vetor.append(int(input('Digite um inteiro: ')))

for elemento in vetor:
    if elemento == 0:
        vetor.remove(elemento)

print(f'\n{vetor}')
