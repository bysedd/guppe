nome1 = input("Nome do arquivo de entrada: ")
with open(nome1, "a") as f:
    while True:
        cidade = input("\nDigite o nome da cidade: ").title()
        habitantes = int(input("Digite o número de habitantes (0 para sair): "))
        if habitantes == 0:
            break
        f.write(f"{cidade}-{habitantes}\n")
        print("Dados salvos.")

with open("arq-entrada.txt") as entrada:
    cidades = []
    for c in entrada.readlines():
        cidade = c.split("\n")[0].split("-")[0]
        habitantes = int(c.split("\n")[0].split("-")[1])
        cidades.append((cidade, habitantes))
    maior_cidade = max(cidades, key=lambda x: x[1])

    nome2 = input("\nNome do arquivo de saída: ")
    with open("arq-saida.txt", "w") as saida:
        saida.write("=" * 20)
        saida.write("\nCIDADE MAIS POPULOSA\n")
        saida.write("=" * 20)
        saida.write(f"\nCidade: {maior_cidade[0]}\n"
                    f"Número de habitantes: {maior_cidade[1]:,.0f}")

print("\nFIM!")
