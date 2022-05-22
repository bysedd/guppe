v = int(input('Digite a quantidade de vezes: '))
n = int(input(f'Digite o 1° número: '))
maior, maior_count = n, 1

for c in range(2, v + 1):
    n = int(input(f'Digite o {c}° número: '))
    if n > maior:
        maior = n
        maior_count += 1

print(f'\nO maior número foi \033[0:34m{maior}\033[m')
print(f'Quantidade de vezes em que o maior número foi lido: \033[0:34m{maior_count}\033[m')
