acres = float(input('Acres: '))
m2 = acres * 4048.58
decimal_places = len(str(acres).split('.')[1])

print(f'acres --> m² = \033[4:32m{m2:.{decimal_places}f}m²\033[m')
