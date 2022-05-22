def m(var, style: int, color: int):
    return f'\033[{style}:{color}m{var}\033[m'


n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0 and c == 11:
        print(f'{m(n, 0, 34)} é múltiplo de {m(11, 1, 33)}')
        break
    elif n % c == 0 and c == 13:
        print(f'{m(n, 0, 34)} é múltiplo de {m(13, 1, 33)}')
        break
    elif n % c == 0 and c == 17:
        print(f'{m(n, 0, 34)} é múltiplo de {m(17, 1, 33)}')
        break
