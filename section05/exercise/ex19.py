n = int(input('Enter an integer: '))

if n % 3 == 0:
    print(f'\033[0:34m{n}\033[m is divisible by \033[1:37m3\033[m')
    print(f'\033[0:34m{n}\033[m / \033[1:37m3\033[m = \033[0:32m{int(n / 3)}\033[m')
elif n % 5 == 0:
    print(f'\033[0:34m{n}\033[m is divisible by \033[1:37m5\033[m')
    print(f'\033[0:34m{n}\033[m / \033[1:37m5\033[m = \033[0:32m{int(n / 5)}\033[m')
else:
    print(f"\033[0:34m{n}\033[m\033[0:31m isn't divisible by\033[m"
          f" \033[1:37m3\033[m\033[0:31m or\033[m \033[1:37m5\033[m")
