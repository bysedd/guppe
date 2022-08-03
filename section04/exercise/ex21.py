libras = float(input('Pounds: '))
kg = libras * 0.45
decimal_places = len(str(libras).split('.')[1])

print(f'\nPounds: \033[4:36m{libras}lb\033[m')
print(f'Kilograms: \033[4:32m{kg:.{decimal_places}f}kg\033[m')
