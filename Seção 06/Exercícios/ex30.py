n, s, p = int(input('Enter an integer greater than 0: ')), 0, ''
if n > 0:
    for c in range(1, n + 1):
        p += f'{c} + '
        s += c
    print(f'{p[:len(p) - 3]} = \033[1:32m{s}\033[m')
    s, p = 0, ''
    for c in range(1, n + 1):
        if c % 2 != 0:
            p += f'{c} - '
            s += c
        elif c % 2 == 0:
            p += f'{c} + '
            s -= c
        elif c == n:
            p += f'{c}'
            s += 2 * n - 1
    print(f'{p[:len(p) - 3]} = \033[1:32m{s}\033[m')
    s, p = 0, ''
    for c in range(1, n + 1, 2):
        p += f'{c} + '
        s += c
    print(f'{p[:len(p) - 3]} = \033[1:32m{s}\033[m')
else:
    print('\033[1:31mInvalid number\033[m')
