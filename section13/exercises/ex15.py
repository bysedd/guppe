from functions import get_idade

with open("nome-data_nascimento.txt") as f:
    pessoas = {}
    for linha in f.readlines():
        linha = linha.split("\n")[0].split("-")
        nome = linha[0].strip().title()
        data_nascimento = linha[1]
        pessoas[nome] = get_idade(data_nascimento)

with open("nome-idade2.txt", "w") as f:
    for nome, idade in pessoas.items():
        f.write(f"{nome:<41}")
        if idade < 18:
            f.write("menor de idade\n")
        elif idade > 18:
            f.write("maior de idade\n")
        else:
            f.write("entrando na maior idade\n")
