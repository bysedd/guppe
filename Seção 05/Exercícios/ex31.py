altura = float(input('Altura(m): '))
peso = int(input('Peso(kg): '))

print('\033[0:34mCategoria:\033[m\033[1:37m')
if altura < 1.20:
    if peso < 60:
        print('A')
    elif peso <= 90:
        print('D')
    else:
        print('G')
elif altura <= 1.70:
    if peso < 60:
        print('B')
    elif peso <= 90:
        print('E')
    else:
        print('H')
else:
    if peso < 60:
        print('C')
    elif peso <= 90:
        print('F')
    else:
        print('I')
