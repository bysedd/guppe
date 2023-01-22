from functions import str_to_bin, float_to_bin

with open("nome-nota_final.txt") as f:
    alunos = {}
    for linha in f.readlines():
        linha = linha.split("\n")[0].split()
        nome, nota_final = " ".join(linha[:-1]), float(linha[-1])
        alunos[nome] = nota_final

with open("nome-nota_final.bin", "w") as f:
    for nome, nota_final in alunos.items():
        # escrevendo só o primeiro nome + nota final
        f.write(f"{str_to_bin(nome.split()[0]):<80} {float_to_bin(nota_final)}\n")
