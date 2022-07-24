vetor = list()

for c in range(1, 16):
    while True:
        media = float(input(f'Digite a nota do {c}º aluno: '))
        if 0.0 <= media <= 10.0:
            vetor.append(media)
            break
        else:
            print('\033[0:31mNota inválida!\033[m')

media_geral = sum(vetor) / len(vetor)
print(f'\nMédia geral: {media_geral:.1f}')
