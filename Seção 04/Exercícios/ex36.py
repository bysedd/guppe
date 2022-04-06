from math import pi, pow

altura = float(input('Height of a circular cylinder: '))
raio = float(input('Radius of a circular cylinder: '))
volume = pi * pow(raio, 2) * altura
decimal_places = len(str(raio).split('.')[1])

if decimal_places < len(str(altura).split('.')[1]):
    decimal_places = len(str(altura).split('.')[1])

print(f'The volume of this circular cylinder is: '
      f'\033[1:32m{volume:.{decimal_places}f}\033[m')
