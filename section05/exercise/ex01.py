n1 = float(input('Enter a number: '))
n2 = float(input('Enter another number: '))

if n1 > n2:
    print(f'\033[0:36m{n1}\033[m is bigger than \033[0:36m{n2}\033[m')
elif n2 > n1:
    print(f'\033[0:36m{n2}\033[m is bigger than \033[0:36m{n1}\033[m')
else:
    print('\033[1:37mBoth are equals\033[m')
