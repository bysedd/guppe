h = float(input('Height: '))
g = input('Gender (m/w): ')

if g[0] == 'm':
    ideal_weight = 72.7 * h - 58
    print(f'Ideal weight is \033[1:34m{ideal_weight:.1f}\033[m')
elif g[0] == 'w':
    ideal_weight = 62.1 * h - 44.7
    print(f'Ideal weight is \033[1:34m{ideal_weight:.1f}\033[m')
else:
    print('\033[0:31mInvalid gender\033[m')
