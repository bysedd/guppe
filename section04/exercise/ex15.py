from math import degrees

rad = float(input('Radians: '))
decimal_places = len(str(rad).split('.')[1])

print(f'\033[0:36m{rad:.{decimal_places}f}rad\033[m = \033[0:32m{int(degrees(rad))}°\033[m')
