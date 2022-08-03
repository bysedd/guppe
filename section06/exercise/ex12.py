n = int(input('Início: '))

for i in range(n, -1, -1):
    print(f'\033[0:34m{i}\033[m', end=' ')
