jardas = float(input('Yards: '))
metros = 0.91 * jardas
decimal_places = len(str(jardas).split('.')[1])

print(f'Yards -> Meters: \033[0:32m{metros:.{decimal_places}f}\033[m')
