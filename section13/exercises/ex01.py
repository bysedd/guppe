print("Para sair digite '0'")
with open("arq.txt", "w+") as f:
    while True:
        try:
            caractere = input("Digite um caractere: ")[0]
            if caractere == "0":
                break
            else:
                f.write(f"{caractere}\n")
        except IndexError:
            print("\033[31mDigite um caractere válido\033[m")

print("\nCaracteres no arquivo:")
with open("arq.txt") as f:
    print(f.read())
