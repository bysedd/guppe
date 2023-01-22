with open("numeros-binarios.txt", "a") as f:
    [f.write(f"{bin(n)[2:]}\n") for n in [int(input(f"Digite o {i}º número inteiro: ")) for i in range(1, 11)]]
