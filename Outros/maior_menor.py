def casas_decimais(lista: list):
    cd = len(str(lista[0]).split('.')[1])
    for valor in lista:
        if len(str(valor).split('.')[1]) > cd:
            cd = len(str(valor).split('.')[1])
    return cd


try:
    n = int(input('Quantos valores irá digitar? '))
    v = float(input('Digite um valor: '))
    valores = [v]
    for _ in range(n - 1):
        v = float(input('Digite outro valor: '))
        valores.append(v)
    cddp = casas_decimais(valores)  # Casas decimais depois do ponto
    print(f'\nValores digitados: {len(valores)}')
    print(f'Maior valor: {max(valores)}')
    print(f'Menor valor: {min(valores)}')
    print(f'Soma de todos os valores: {sum(valores):.{cddp}f}')
except ValueError:
    print('\033[1:31mValor inválido!\033[m')
