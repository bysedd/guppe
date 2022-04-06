kelvin = float(input('Temperature in degrees Kelvin: '))
celsius = kelvin - 273.15

print(f'\033[1:32m{kelvin:.1f}K\033[m equals \033[1:36m{celsius:.1f}°C\033[m')
