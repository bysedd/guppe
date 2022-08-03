soma, a, b, c = 0, 0, 0, 0
frase = ''

for c in range(0, 3):
    numero = int(input("Enter an integer value: "))

    """ Não existe switch em Python :(
    switch(c):
        case 0:
            a = numero
            frase += f'\033[1:36m{numero}\033[m + '
            break
        case 1:
            b = numero
            frase += f'\033[1:36m{numero}\033[m + '
            break
        case 2:
            c = numero
            frase += f'\033[1:36m{numero}\033[m + '
            break
    """
    if c == 0:
        a = numero
        frase += f'\033[1:36m{numero}\033[m + '
    elif c == 1:
        b = numero
        frase += f'\033[1:36m{numero}\033[m + '
    else:
        c = numero
        frase += f'\033[1:36m{numero}\033[m'

    soma += numero

print(f'{frase} = \033[1:32m{soma}\033[m')
