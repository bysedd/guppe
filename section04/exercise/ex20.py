kg = float(input('Kilograms: '))
libras = kg / 0.45
decimal_places = len(str(kg).split('.')[1])

print(f'\nKilograms: \033[4:36m{kg}kg\033[m')
print(f'Pounds: \033[5:32m{libras:.{decimal_places}f}lb\033[m')
