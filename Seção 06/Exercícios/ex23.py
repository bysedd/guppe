n, c = int(input('Digite um número: ')), 0
print(f'\033[0:34m{n}\033[m pode ser divido por:', end=' ')
for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[0:34m{i}\033[m', end=' ')
        c += 1
print(f'\nPode ser dividido por \033[0:34m{c}\033[m números distintos')
