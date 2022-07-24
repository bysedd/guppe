num = list()
impar = list()

for _ in range(10):
    num.append(int(input('Digite um inteiro entre [0,50]: ')))

for elemento in num:
    if elemento % 2 != 0:
        impar.append(elemento)

print()
for i in range(len(impar)):
    print(num[i], impar[i])
