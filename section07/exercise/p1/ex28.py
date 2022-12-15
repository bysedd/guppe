v = []

for _ in range(10):
    v.append(int(input('Digite um inteiro: ')))

v1 = []
v2 = []

for elemento in v:
    if elemento % 2 == 0:
        v2.append(elemento)
    else:
        v1.append(elemento)

if len(v1) != 0:
    print(f'Ímpares: {v1}')
if len(v2) != 0:
    print(f'Pares: {v2}')
