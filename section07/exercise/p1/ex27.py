lista = []
vetor = []

for _ in range(10):
    lista.append(int(input('Digite um inteiro: ')))

for elemento in lista:
    mult = 0
    for count in range(2, elemento):
        if elemento % count == 0:
            mult += 1
    if mult == 0:
        if elemento > 1:
            vetor.append(elemento)
print()

for primo in vetor:
    print(f'primo={primo}: index={lista.index(primo)}')
