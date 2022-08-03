avg, c = 0.0, 0
while True:
    nota = int(input('Type a note: '))
    if 10 <= nota <= 20:
        c += 1
    else:
        if c != 0:
            avg = nota / c
        break
print(f'\nMédia do aluno: \033[1:34m{avg:.1f}\033[m')
