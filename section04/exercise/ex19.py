l = int(input('Liters: '))
m = l / 1000

print(f'Volume em litros: \033[4:36m{l}L\033[m')
print(f'Volume em metros cúbicos: \033[3:32m{m}m³\033[m')
