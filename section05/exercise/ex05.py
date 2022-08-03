n = int(input('Enter an integer: '))

if n % 2 == 0:
    print(f'\033[0:32m{n} is even\033[m')
else:
    print(f'\033[0:33m{n} is odd\033[m')
