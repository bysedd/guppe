from string import ascii_lowercase
from collections import defaultdict

arquivo = "animals.txt"

# número de caracteres
with open(arquivo) as f:
    caracteres = 0
    for linha in f.readlines():
        linha = linha.split()
        caracteres += len("".join(linha))
    print(f"Quantidade de caracteres: {caracteres}")

# número de linhas
with open(arquivo) as f:
    print(f"Quantidade de linhas: {len(f.readlines())}")

# número de palavras
with open(arquivo) as f:
    palavras = 0
    for linha in f.readlines():
        linha = linha.split()
        palavras += len(linha)
    print(f"Quantidade de palavras: {palavras}")

# contagem de letras
with open(arquivo) as f:
    alfabeto = defaultdict(int)
    for linha in f.readlines():
        linha = linha.split()
        for palavra in linha:
            for letra in palavra:
                letra = letra.lower()
                if letra in ascii_lowercase:
                    alfabeto[letra] += 1
    alfabeto = sorted(alfabeto.items())
    print("Contagem de letras:")
    [print("\t" * 5 + k, v, sep=" => ") for k, v in alfabeto]
