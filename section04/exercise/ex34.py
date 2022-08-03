raio = float(input('Circle radius: '))
area = 3.141592 * (raio * raio)
decimal_places = len(str(raio).split('.')[1])

print(f'The area of the circle is: \033[0:36m{area:.{decimal_places}f}\033[m')
