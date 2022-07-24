lista = []

for i in range(3):
    numero = int(input(f'Número do {i + 1}º aluno: '))
    altura = float(input('Altura em metros: '))
    lista.append({'id': numero, 'altura': altura})
    print()

maior_altura = lista[0].get('altura')
id_maior = lista[0].get('id')

menor_altura = lista[0].get('altura')
id_menor = lista[0].get('id')

for elemento in lista:
    if elemento.get('altura') > maior_altura:
        maior_altura = elemento.get('altura')
        id_maior = elemento.get('id')
    if elemento.get('altura') < menor_altura:
        menor_altura = elemento.get('altura')
        id_menor = elemento.get('id')

print(f'\nAluno mais alto: id={id_maior}: altura={maior_altura:.2f}')
print(f'Aluno mais baixo: id={id_menor}: altura={menor_altura:.2f}')
