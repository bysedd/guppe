nota = float(input('Nota do aluno(a): '))
falta = int(input('Falta(s) do aluno(a): '))
conceito = ''

if nota > 10.0 or nota < 0.0:
    print('\033[0:31mNota inválida\033[m')
    if falta < 0:
        print('Falta\033[0:31m precisa ser >= 0\033[m')
elif falta < 0:
    print('Falta\033[0:31m precisa ser menor ou igual a 0\033[m')
    if nota > 10.0 or nota < 0.0:
        print('\033[0:31mNota inválida')
else:
    if 9.0 <= nota <= 10.0:
        if falta <= 20:
            conceito = 'A'
        else:
            conceito = 'B'
    elif 7.5 <= nota <= 8.9:
        if falta <= 20:
            conceito = 'B'
        else:
            conceito = 'C'
    elif 5.0 <= nota <= 7.4:
        if falta <= 20:
            conceito = 'C'
        else:
            conceito = 'D'
    elif 4.0 <= nota <= 4.9:
        if falta <= 20:
            conceito = 'D'
        else:
            conceito = 'E'
    elif 0.0 <= nota <= 3.9:
        if falta <= 20:
            conceito = 'E'
        else:
            conceito = 'E'

    print(f'O conceito do aluno(a) é: \033[0:34m{conceito}\033[m')
