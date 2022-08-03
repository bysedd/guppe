v = int(input('\033[0:34m1°\033[m valor: '))
maior, menor = v, v
for i in range(2, 11):
    v = int(input(f'\033[0:34m{i}°\033[m valor: '))
    if v > maior:
        maior = v
    elif v < menor:
        menor = v
print(f'\nMaior valor: \033[0:34m{maior}\033[m\nMenor valor: \033[0:34m{menor}\033[m')
