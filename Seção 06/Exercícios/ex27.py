n = int(input('Enter an integer: '))
if n > 0:
    h = 1
    for c in range(2, n + 1):
        h += 1 / c
    print(f'\033[0:34mH({n})\033[m = \033[1:32m{h:.1f}\033[m')
else:
    print('\033[1:31mO número precisa ser positivo\033[m')
