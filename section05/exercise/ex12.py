from math import log10

n = int(input('Enter an integer: '))

if n > 0:
    print(f'log({n}) = {log10(n)}')
else:
    print('\033[0:31mInvalid number\033[m')
