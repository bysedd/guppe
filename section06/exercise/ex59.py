n = int(input('Número de habitantes de uma determinada cidade: '))
valor_kwh = float(input('Valor do kwh: \033[3:34mR$\033[m'))
nome_categoria = {
    1: 'residencial',
    2: 'comercial',
    3: 'industrial',
}
total_categoria = {
    1: 0.0,
    2: 0.0,
    3: 0.0
}
consumo = float(input('\nConsumo de energia do mês:\033[3:34m kwh\033[m'))
codigo = int(input('1-Residencial; 2-Comercial; 3-Industrial\nCódigo do consumidor: '))
consumo *= valor_kwh
if codigo == 1:
    total_categoria[1] += consumo
elif codigo == 2:
    total_categoria[2] += consumo
elif codigo == 3:
    total_categoria[3] += consumo
else:
    while codigo not in (1, 2, 3):
        print(f'\033[1:31mCódigo inválido\033[m')
        codigo = int(input('1-Residencial; 2-Comercial; 3-Industrial\nCódigo do consumidor: '))
        if codigo == 1:
            total_categoria[1] += consumo
        elif codigo == 2:
            total_categoria[2] += consumo
        elif codigo == 3:
            total_categoria[3] += consumo
maior, menor, total = consumo, consumo, consumo
cont = 1

for _ in range(2, n + 1):
    consumo = float(input('\nConsumo de energia do mês:\033[3:34m kwh\033[m'))
    codigo = int(input('1-Residencial; 2-Comercial; 3-Industrial\nCódigo do consumidor: '))
    consumo *= valor_kwh
    if codigo == 1:
        total_categoria[1] += consumo
    elif codigo == 2:
        total_categoria[2] += consumo
    elif codigo == 3:
        total_categoria[3] += consumo
    else:
        while codigo not in (1, 2, 3):
            print(f'\033[1:31mCódigo inválido\033[m')
            codigo = int(input('1-Residencial; 2-Comercial; 3-Industrial\nCódigo do consumidor: '))
            if codigo == 1:
                total_categoria[1] += consumo
            elif codigo == 2:
                total_categoria[2] += consumo
            elif codigo == 3:
                total_categoria[3] += consumo
    if consumo > maior:
        maior = consumo
    elif consumo < menor:
        menor = consumo
    cont += 1
    total += consumo
media = total / cont
print(f'\nMaior consumo: \033[3:32mR${maior:.2f}\033[m')
print(f'Menor consumo: \033[3:32mR${menor:.2f}\033[m')
print(f'Média do consumo dos habitantes: \033[3:32mR${media:.2f}\033[m\n')
for i in range(1, 4):
    print(f'Total da categoria \033[3:34m{nome_categoria[i]}\033[m \033[3:32mR${total_categoria[i]:.2f}\033[m')
