"""
Escrevendo em arquivos CSV

reader (leitor) -> writer (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para podermos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.

with open(r'section18\filmes.csv', 'w', encoding='utf-8') as f:
    escritor_csv = csv.writer(f)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])

    while filme != 'Sair':
        filme = input('Informe o nome do filme (sair): ').strip().title()
        if filme != 'Sair':
            genero = input('Informe o gênero: ').strip().title()
            duracao = input('Informe a duração (em minutos): ').strip().title()
            escritor_csv.writerow([filme, genero, duracao])

"""

import csv

# DictWriter ≥ Permite que escrevamos em um arquivo CSV utilizando um dicionário como
# base para a escrita. Possui um parâmetro opcional que é o fieldnames, ou seja, uma lista
# com os nomes das colunas. Caso não informemos este parâmetro, as chaves do dicionário
# serão utilizadas como nome das colunas.

# OBS: as chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

with open('filmes.csv', 'w', encoding='utf-8') as f:
    escritor_csv = csv.DictWriter(f, fieldnames=['Título', 'Gênero', 'Duração'])
    escritor_csv.writeheader()
    filme = None
    while filme != 'Sair':
        try:
            filme = input('Informe o nome do filme (sair): ').strip().title()
            if filme != 'Sair':
                genero = input('Informe o gênero: ').strip().title()
                duracao = int(input('Informe a duração (em minutos): '))
                escritor_csv.writerow({
                    "Título": filme,
                    "Gênero": genero,
                    "Duração": duracao
                })
        except ValueError:
            print('Duração inválida. Informe apenas números inteiros.')
        print()
