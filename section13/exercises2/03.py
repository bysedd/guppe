vogais = 0

with open("arq.txt", encoding="UTF-8") as f:
    for letra in f.readlines():
        letra = letra.split("\n")[0]
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais += 1

print(f"Quantidade de vogais no arquivo: {vogais}")
