c = float(input('Length: '))
L = float(input('Width: '))
p = float(input('Fabric price R$'))

terreno = c * L
total = terreno * p

print(f'Cost to fence this land \033[0:32mR${total:.2f}\033[m')
