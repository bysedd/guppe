vetor = []

for _ in range(6):
    while True:
        numero = int(input('Digite um número inteiro: '))
        if numero % 2 == 0:
            vetor.append(numero)
            break

print(vetor)
print(vetor[::-1])
