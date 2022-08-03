from math import radians

degrees = float(input('Angle degrees: '))
rad = radians(degrees)

print(f'\033[0:36m{int(degrees)}°\033[m = \033[0:32m{rad:.3f}rad\033[m')
