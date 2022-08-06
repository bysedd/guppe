num = [int(input('Digite um inteiro: ')) for _ in range(10)]
impar = list()

for elemento in num:
    if elemento % 2 != 0:
        impar.append(elemento)

print()
for i in range(len(impar)):
    print(num[i], impar[i])
