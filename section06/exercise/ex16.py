n = int(input('Digite um número inteiro positivo ímpar: '))

if n >= 0 and n % 2 != 0:
    for c in range(n, 0, -1):
        if c % 2 != 0:
            print(f'\033[0:34m{c}\033[m', end=' ')
else:
    print('\033[0:31mNúmero inválido\033[m')
