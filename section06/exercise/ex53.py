n = int(input('Digite um número inteiro positivo: '))
i = 1
for c in range(1, n + 1):
    for j in range(1, c + 1):
        print(f'\033[3:34m{i}\033[m', end=' ')
        i += 1
    print()
