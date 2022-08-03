r, r1, r2 = 0, 0, 0
while True:
    x = int(input('Resistor 1: '))
    y = int(input('Resistor 2: '))
    if x == 0 or y == 0:
        break
    else:
        r1, r2 = x, y
        r = (r1 * r2) / (r1 + r2)
        print()
if r1 == 0 and r2 == 0:
    print('\033[0:31mDigite valores positivos primeiramente\033[m')
else:
    print(f'\nAssociação em paralelo de dois resistores '
          f'\033[0:34m{r1}\033[m e \033[0:34m{r2}\033[m é \033[1:32m{r:.1f}\033[m')
