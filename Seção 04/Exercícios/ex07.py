fahrenheit = float(input('Temperature in degrees Fahrenheit: '))
celsius = 5 * (fahrenheit - 32) / 9

print(f'\033[1:32m{fahrenheit:.1f}°F\033[m equals \033[1:36m{celsius:.1f}°C\033[m')
