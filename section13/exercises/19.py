with open("nome-nota.txt", encoding="utf-8") as f:
    alunos = {}
    for linha in f.readlines():
        linha = linha.split("\n")[0].split("|")
        nome = " ".join(linha[0].split()[1:]).strip().title()
        nota = float(linha[1].split()[1])
        alunos[nome] = nota
    [print(aluno) for aluno in alunos.items()]
    print(f"\nO aluno que possui a maior nota é: {max(alunos.items(), key=lambda x: x[1])}")
