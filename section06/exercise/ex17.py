n = int(input('Digite um número inteiro positivo: '))
s = 0

if n >= 0:
    for c in range(0, n + 1):
        print(f'\033[0:34m{c}\033[m', end=' ')
        s += c
print(f'\nA soma de todos os números naturais é \033[0:32m{s}\033[m')
