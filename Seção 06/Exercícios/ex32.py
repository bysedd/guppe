from random import randint

n = int(input('Número de vezes: '))
maior = int(input('Maior número do dado: '))
for c in range(1, n + 1):
    print(f'\033[1:34m\n{c}° tentativa.\033[m')
    d1, d2 = randint(1, maior), randint(1, maior)
    if d1 > d2:
        print(f'\033[1:32m{d1}\033[m > \033[1:31m{d2}\033[m')
    elif d1 < d2:
        print(f'\033[1:31m{d1}\033[m < \033[1:32m{d2}\033[m')
    else:
        print(f'\033[1:33m{d1}\033[m = \033[1:33m{d2}\033[m')
