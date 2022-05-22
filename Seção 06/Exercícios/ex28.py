from math import factorial

n = int(input('Enter an integer: '))
if n > 0:
    e = 1
    for c in range(1, n + 1):
        e += 1 / factorial(c)
    print(f'\033[0:34mE({n})\033[m = \033[1:32m{e:.1f}\033[m')
else:
    print('\033[1:31mO número precisa ser positivo\033[m')
