def azul(num: int):
    return f'\033[0:34m{num}\033[m'


s = 0
for c in range(1, 1000 + 1):
    if c % 3 == 0 or c % 5 == 0:
        s += c
print(f'A soma de todos os números naturais abaixo de {azul(1000)} que são múltiplos de '
      f'{azul(3)} ou {azul(5)} é: \033[1:32m{s}\033[m')
