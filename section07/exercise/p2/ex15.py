def linha():
    print('-=' * 32)


def programa():
    from random import choice
    alternativas = [[], [], [], [], []]
    gabarito = []
    for i in range(5):
        for j in range(10):
            alternativas[i].append(choice(('a', 'b', 'c', 'd')))
    alunos = {
        'Aluno 1': alternativas[0],
        'Aluno 2': alternativas[1],
        'Aluno 3': alternativas[2],
        'Aluno 4': alternativas[3],
        'Aluno 5': alternativas[4]
    }
    for _ in range(10):
        gabarito.append(choice(('a', 'b', 'c', 'd')))
    linha()
    print(f'Gabarito:   {gabarito}')
    linha()
    for a in alunos.items():
        print(a)
    linha()
    i = 1
    for a in alunos.values():
        pontos = 0
        for c in range(10):
            if a[c] == gabarito[c]:
                pontos += 1
        print(f'Aluno {i} obteve nota {pontos}')
        i += 1
    linha()


programa()
