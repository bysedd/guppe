print("""\033[1:32m1: Soma\033[m
\033[1:33m2: Subtração\033[m
\033[1:35m3: Multiplicação\033[m
\033[1:36m4: Divisão\033[m""")
p = int(input('\nEscolha uma opção: '))
print()

if p == 1:
    print('Você escolheu\033[1:32m soma\033[m')
    x = float(input('Digite um valor: '))
    y = float(input('Digite outro valor: '))
    xl = len(str(x).split('.')[1])
    yl = len(str(y).split('.')[1])

    if xl > yl:
        print(f'\033[0:34m{x}\033[m + \033[0:34m{y}\033[m = \033[1:37m{(x + y):.{xl}f}\033[m')
    else:
        print(f'\033[0:34m{x}\033[m + \033[0:34m{y}\033[m = \033[1:37m{(x + y):.{yl}f}\033[m')
elif p == 2:
    print('Você escolheu\033[1:33m subtração\033[m')
    x = float(input('Digite um valor: '))
    y = float(input('Digite outro valor: '))
    xl = len(str(x).split('.')[1])
    yl = len(str(y).split('.')[1])

    if xl > yl:
        print(f'\033[0:34m{x}\033[m - \033[0:34m{y}\033[m = \033[1:37m{(x - y):.{xl}f}\033[m')
    else:
        print(f'\033[0:34m{x}\033[m - \033[0:34m{y}\033[m = \033[1:37m{(x - y):.{yl}f}\033[m')
elif p == 3:
    print('Você escolheu\033[1:35m multiplicação\033[m')
    x = float(input('Digite um valor: '))
    y = float(input('Digite outro valor: '))
    xl = len(str(x).split('.')[1])
    yl = len(str(y).split('.')[1])

    if xl > yl:
        print(f'\033[0:34m{x}\033[m * \033[0:34m{y}\033[m = \033[1:37m{(x * y):.{xl}f}\033[m')
    else:
        print(f'\033[0:34m{x}\033[m * \033[0:34m{y}\033[m = \033[1:37m{(x * y):.{yl}f}\033[m')
elif p == 4:
    print('Você escolheu\033[1:36m divisão\033[m')
    x = float(input('Digite um valor: '))
    y = float(input('Digite outro valor: '))
    xl = len(str(x).split('.')[1])
    yl = len(str(y).split('.')[1])

    if xl > yl:
        print(f'\033[0:34m{x}\033[m / \033[0:34m{y}\033[m = \033[1:37m{(x / y):.{xl}f}\033[m')
    else:
        print(f'\033[0:34m{x}\033[m / \033[0:34m{y}\033[m = \033[1:37m{(x / y):.{yl}f}\033[m')
else:
    print('\033[1:31mOpção inválida!\033[m')
