hectares = float(input('hectares: '))
m2 = hectares * 10000
decimal_places = len(str(hectares).split('.')[1])

print(f'hectares --> m² = \033[4:32m{m2:.{decimal_places}f}he\033[m')
