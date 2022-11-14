caractere = input("Digite um caractere: ")[0]
cont = 0

with open("arq.txt", encoding="UTF-8") as f:
    for c in f.readlines():
        c = c.split(r"\n")[0]
        if c == caractere:
            cont += 1

print(f"O caractere '{caractere}' aparece {cont} vez(es) neste arquivo.")
