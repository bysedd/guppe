vetor = []
d = {}

for _ in range(10):
    vetor.append(int(input('Digite um número inteiro: ')))

for num in vetor:
    if num >= 0:
        d[num] = num
    else:
        d[num] = 0

print()
for chave, valor in d.items():
    print(f'{chave}: {valor}')
