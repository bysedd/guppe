numero_de_alunos = int(input("Número de alunos de uma disciplina: "))
alunos = {}

for i in range(1, numero_de_alunos + 1):
    nome = input(f"\nNome do {i}º aluno: ").strip().title()
    nota_final = float(input(f"Nota final do {i}º aluno: "))
    alunos[nome] = nota_final

with open("nome-nota_final.txt", "w") as f:
    [f.write(f"{nome:<40} {nota_final}\n") for nome, nota_final in alunos.items()]
