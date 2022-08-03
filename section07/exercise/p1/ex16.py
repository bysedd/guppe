vetor = []

for _ in range(5):
    vetor.append(float(input('Digite um número real: ')))

while True:
    c = int(input('\n0 - Finaliza o programa.\n'
                  '1 - Mostra o vetor na ordem direta.\n'
                  '2 - Mostra o vetor na ordem inversa.\n'
                  '3 - Atualizar vetor.\n'
                  'Código: '))
    if c == 0:
        break
    elif c == 1:
        print(vetor)
    elif c == 2:
        print(vetor[::-1])
    elif c == 3:
        vetor.clear()
        for _ in range(5):
            vetor.append(float(input('\nDigite um número real: ')))
    else:
        print('\033[0:31mCódigo inválido!\033[m')
