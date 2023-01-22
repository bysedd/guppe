from functions import get_idade

with open("nome-data_nascimento.txt") as f:
    pessoas = {}
    for linha in f.readlines():
        linha = linha.split("-")

        nome = linha[0].strip().title()
        data_nascimento = linha[1]

        pessoas[nome] = get_idade(data_nascimento)

with open("nome-idade.txt", "w") as f:
    for nome, idade in pessoas.items():
        f.write(f"{nome:<40} {idade} anos\n")
