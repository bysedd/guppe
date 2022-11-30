with open("nome-preco.txt", encoding="utf-8") as f:
    produtos = {}
    for linha in f.readlines():
        linha = linha.split("\n")[0]
        nome, preco = linha.split("-")
        produtos[nome] = float(preco)
    [print(f"{k} R${v:,.2f}") for k, v in produtos.items()]
    print(f"\nTotal: R${sum(produtos.values())}")
