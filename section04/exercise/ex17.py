c = float(input('Centimeters: '))
p = c / 2.54
decimal_places = len(str(c).split('.')[1])

print(f"\033[0:36m{c}cm\033[m equal's \033[0:32m{p:.{decimal_places}f}in\033[m")
