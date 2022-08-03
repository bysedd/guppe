# -<°-°>- Incompreensível
soma = 0
for m in (0, 1):
    if m == 1:
        soma += 3
    for c in range(0, 10):
        if c == 1:
            soma += 3
        elif c == 2:
            soma += 8
        elif c == 3:
            soma += 9
        elif c == 4:
            soma += 12
        elif c == 5:
            soma += 10
        elif c == 6:
            soma += 10
        elif c == 7:
            soma += 10
        elif c == 8:
            soma += 10
        elif c == 9:
            soma += 10
        for d in range(0, 10):
            if c == 1:
                soma += 3
            elif c == 2:
                soma += 5
            elif c == 3:
                soma += 6
            elif c == 4:
                soma += 8
            elif c == 5:
                soma += 9
            elif c == 6:
                soma += 8
            elif c == 7:
                soma += 7
            elif c == 8:
                soma += 7
            elif c == 9:
                soma += 7
            for u in range(0, 10):
                if c == 1:
                    soma += 2
                elif c == 2:
                    soma += 4
                elif c == 3:
                    soma += 4
                elif c == 4:
                    soma += 6
                elif c == 5:
                    soma += 5
                elif c == 6:
                    soma += 4
                elif c == 7:
                    soma += 4
                elif c == 8:
                    soma += 4
                elif c == 9:
                    soma += 4
print(f'Se \033[3:31m1 a 1000\033[m fossem escritos em palavras seriam utilizadas \033[3:34m{soma} letras\033[m')
