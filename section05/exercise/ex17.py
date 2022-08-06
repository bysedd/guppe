lb = float(input('Base menor: '))
sb = float(input('Base menor: '))
height = float(input('Altura: '))

if lb > 0 and sb > 0:
    a = (lb + sb) * height / 2
    print(f'A área do trapézio é \033[0:34m{a:.2f}\033[m')
else:
    print('\033[0:31mA base menor ou a base menor devem ser maiores que 0\033[m')
