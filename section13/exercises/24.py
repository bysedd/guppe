import pandas as pd
from functions import print_formatado, error_message

opcoes = {
    1: "Entrada de produtos",
    2: "Retirada de produtos",
    3: "Relátorio geral",
    4: "Produtos não disponíveis",
    5: "Sair"
}
produtos = []
with open("despensa-domestica.bin") as f:
    for linha in f.readlines():
        linha = linha.split("\n")[0].split(";")
        codigo, nome, quantidade = int(linha[0]), linha[1], int(linha[2])
        produtos.append([codigo, nome, quantidade])
df = pd.DataFrame(produtos, columns=["codigo", "nome", "quantidade"])

while True:
    [print(k, v, sep=" - ") for k, v in opcoes.items()]
    opt = int(input("Escolha uma opção: "))

    while True:
        match opt:
            case 1:
                while True:
                    try:
                        ...
                    except ValueError as err:
                        print(error_message(err) + "\n")

            case 2:
                pass
            case 3:
                print_formatado("Relatório geral")
                print(df.to_string(index=False))
                break
            case 4:
                pass
            case 5:
                break
            case _:
                print("Opção inválida")
