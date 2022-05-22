n, s, p = int(input('Digite um número: ')), 0, ''
print(f'A soma dos divisores do número \033[0:34m{n}\033[m é:', end=' ')
for i in range(1, n):
    if n % i == 0:
        p += f'\033[0:34m{i}\033[m + '
        s += i
print(f'{p[:len(p) - 3]} = \033[1:32m{s}\033[m')
