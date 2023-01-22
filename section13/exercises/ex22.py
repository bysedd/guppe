with open("nome-notas-entrada.txt") as f:
    alunos = {}
    for linha in f.readlines():
        linha = linha.split("\n")[0].split("|")
        nome = linha[0]
        notas = [float(nota) for nota in linha[1].split()]
        alunos[nome] = notas
    for k, v in alunos.items():
        alunos[k] = sorted(v)

with open("nome-notas-saida.txt", "w") as f:
    for nome, notas in alunos.items():
        f.write(f"{nome:<40} {notas}\n")
