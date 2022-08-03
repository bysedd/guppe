while True:
    op = int(input("""adição (opção 1)
subtração (opção 2)
multiplicação (opção 3)
divisão (opção 4)
saída (opção 5)
Opção escolhida: """))
    print()
    if op == 1:
        print('\033[0:34m\tadição\033[m')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
        print(f'\033[0:34m{x}\033[m + \033[0:34m{y}\033[m = \033[0:32m{x + y}\033[m')
    elif op == 2:
        print('\033[0:34m\tsubtração\033[m')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
        print(f'\033[0:34m{x}\033[m - \033[0:34m{y}\033[m = \033[0:32m{x - y}\033[m')
    elif op == 3:
        print('\033[0:34m\tmultiplicação\033[m')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
        print(f'\033[0:34m{x}\033[m * \033[0:34m{y}\033[m = \033[0:32m{x * y}\033[m')
    elif op == 4:
        print('\033[0:34m\tdivisão\033[m')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
        print(f'\033[0:34m{x}\033[m / \033[0:34m{y}\033[m = \033[0:32m{(x / y):.1f}\033[m')
    elif op == 5:
        print('\033[1:37mFinalizado\033[m')
        break
    else:
        print('\033[1:31mOpção inválida\033[m')
    print()
