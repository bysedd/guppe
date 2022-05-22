chico = 1.20
ze = 1.00
a = 0
while ze <= chico:
    chico += 0.02
    ze += 0.03
    a += 1
    """
    print(f'\033[1:37m{a}° ano\033[m')
    print(f'Chico \033[0:34m{chico:.2f}m\033[m')
    print(f'Zé \033[0:34m{ze:.2f}m\033[m\n')
    """
print(f'Serão necessários \033[1:37m{a} anos\033[m para \033[0:34mZé ser maior que Chico\033[m')
