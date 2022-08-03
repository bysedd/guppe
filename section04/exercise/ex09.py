celsius = float(input('Temperature in degrees Celsius: '))
kelvin = celsius + 273.15

print(f'\033[0:36m{celsius:.1f}°C\033[m equals \033[0:32m{kelvin:.1f}K\033[m')
