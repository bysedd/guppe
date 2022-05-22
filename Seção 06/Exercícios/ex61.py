maior = 100 * 100
p = ''
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        a = i * j
        teste = str(a)
        primeira_parte = str(teste[:3])
        segunda_parte = str(teste[3:])
        if segunda_parte == primeira_parte[::-1]:
            if a > maior:
                maior = a
                p = f'{i} * {j} = {teste}'
print(f'Maior palíndromo feito a partir de dois números de 3 dígitos:\n{p}')
