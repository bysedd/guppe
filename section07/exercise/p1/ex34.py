vetor = []

vetor.append(int(input('Digite um inteiro: ')))
while len(vetor) < 10:
    n = int(input('Digite um inteiro: '))
    if n in vetor:
        print('\033[0:31mNúmero já registrado no vetor!\033[m')
    else:
        vetor.append(n)

print(f'\n{vetor}')
