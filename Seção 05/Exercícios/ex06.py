n1 = int(input('Enter an integer: '))
n2 = int(input('Enter another integer: '))

if n1 > n2:
    print(f'\033[0:32m{n1} is greater than {n2}')
    print(f'{n1 - n2} difference number(s)\033[m')
else:
    print(f'\033[0:34m{n2} is greater than {n1}')
    print(f'{n2 - n1} difference number(s)\033[m')
