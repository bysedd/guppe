from math import sqrt, pow

print('--- Catetos de um triângulo ---')

a = float(input('a: '))
b = float(input('b: '))
hipotenusa = sqrt(pow(a, 2) + pow(b, 2))

print(f'Hipotenusa: \033[0:36m{hipotenusa:.2f}\033[m')
