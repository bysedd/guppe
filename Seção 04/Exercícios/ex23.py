metros = float(input('Meters: '))
jardas = metros / 0.91
decimal_places = len(str(metros).split('.')[1])

print(f'Meters --> Yards: \033[0:32m{jardas:.{decimal_places}f}\033[m')
