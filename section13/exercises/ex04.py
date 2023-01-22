vogais = 0
consoantes = 0

with open("arq.txt", encoding="UTF-8") as f:
    for letra in f.readlines():
        letra = letra.split("\n")[0]
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1
        elif letra in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n'
                                                                         'p', 'q', 'r', 't', 's', 'v', 'w', 'x', 'y',
                       'z']:
            consoantes += 1

print(f"Quantidade de vogais no arquivo: {vogais}")
print(f"Quantidade de consoantes no arquivo: {consoantes}")
