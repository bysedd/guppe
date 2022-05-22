km = int(input('Kilometers per hour: '))
litros = int(input('Liters consumed: '))
consumo = km / litros

print(f'Km/l: \033[0:34m{consumo:.1f}\033[m')
if consumo <= 8.0:
    print('\033[0:31mSell the car!\033[m')
elif consumo <= 14.0:
    print('\033[0:32mEconomic!\033[m')
else:
    print('\033[1:32mSuper economic!\033[m')
