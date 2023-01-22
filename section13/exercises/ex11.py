palavra = input("Digite uma palavra: ").lower()
arquivo = "animals.txt"
count = 0

with open(arquivo) as f:
    for linha in f.readlines():
        linha = linha.split()
        for palavra_linha in linha:
            if palavra_linha.lower() == palavra:
                count += 1

print(f"A palavra {palavra} aparece {count} vezes no arquivo '{arquivo}'")
