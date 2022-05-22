from math import sqrt, pow

while True:
    n = int(input('Digite um valor: '))
    if n <= 0:
        print('\033[1:37mFinalizado\033[m')
        break
    else:
        print(f'\033[0:34m{n}²\033[m = \033[0:32m{pow(n, 2)}\033[m')
        print(f'\033[0:34m{n}³\033[m = \033[0:32m{pow(n, 3)}\033[m')
        print(f'\033[0:34m√{n}\033[m = \033[0:32m{sqrt(n):.1f}\033[m\n')
