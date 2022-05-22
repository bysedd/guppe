c, s = 0, 0
while True:
    idade = int(input('Informe uma idade: '))
    if idade > 0:
        c += 1
        s += idade
    else:
        break
media = s / c
print(f'\nIdade média desse grupo: \033[0:34m{media:.1f}\033[m')
