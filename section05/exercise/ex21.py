op = int(input("""Escolha a opção:
\033[0:32m1- Soma de 2 números.\033[m
\033[0:33m2- Diferença entre 2 números (menor pelo menor).\033[m
\033[0:35m3- Produto entre 2 números.\033[m
\033[0:36m4- Divisão entre 2 números (o denominador não pode ser zero).\033[m
Opção: """))
print()

if op == 1:
    print('\033[0:32mSum:\033[m')
    a = float(input('A: '))
    b = float(input('B: '))
    print(f'\033[0:34m{a}\033[m + \033[0:34m{b}\033[m = \033[0:32m{a + b}\033[m')
elif op == 2:
    print('\033[0:33mDiference:\033[m')
    a = float(input('A: '))
    b = float(input('B: '))
    if a > b:
        print(f'\033[0:34m{a}\033[m - \033[0:34m{b}\033[m = \033[0:33m{a - b}\033[m')
    else:
        print(f'\033[0:34m{b}\033[m - \033[0:34m{a}\033[m = \033[0:33m{b - a}\033[m')
elif op == 3:
    print('\033[0:35mProduct:\033[m')
    a = float(input('A: '))
    b = float(input('B: '))
    print(f'\033[0:34m{a}\033[m * \033[0:34m{b}\033[m = \033[0:35m{a * b}\033[m')
elif op == 4:
    a = float(input('A: '))
    b = float(input('B: '))
    if b == 0:
        print('\033[0:34mB\033[m\033[0:31m cannot be zero\033[m')
    else:
        print(f'{a} / {b} = {a / b}')
else:
    print('\033[0:31mInvalid option\033[m')
