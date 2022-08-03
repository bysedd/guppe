celsius = float(input('Temperature in degrees Celsius: '))
fahrenheit = celsius * 1.8 + 32.0

print(f'\033[1:36m{celsius:.1f}°C\033[m equals \033[1:32m{fahrenheit:.1f}°F\033[m')
