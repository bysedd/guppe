n = int(input('Enter a positive number greater than 0: '))
i = int(input('i: '))
j = int(input('j: '))

if n > 0 and i > 0 and j > 0:
    c, x, p = 1, 0, ''
    while c <= n:
        if x % i == 0 or x % j == 0:
            p += f'\033[0:34m{x}\033[m,'
            c += 1
            x += 1
        else:
            x += 1
    print(p[:len(p) - 1])
else:
    print(f'\033[1:31mInvalid number(s)\033[m')
