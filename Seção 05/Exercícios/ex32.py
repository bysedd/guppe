menu = {
    100: 'Cachorro Quente',
    101: 'Bauru Simples',
    102: 'Bauru com Ovo',
    103: 'Hamburguer',
    104: 'Cheeseburguer',
    105: 'Suco',
    106: 'Refrigerante'
}
price = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.70,
    105: 2.20,
    106: 1.00
}

code = int(input("""100: Cachorro Quente
101: Bauru Simples
102: Bauru com Ovo
103: Hamburguer
104: Cheeseburguer
105: Suco
106: Refrigerante
\033[0:34mCódigo:\033[m """))

if 100 <= code <= 106:
    qtn = int(input('Quantidade: '))
    total = qtn * price.get(code)

    print(f'Total a pagar: \033[0:32mR${total:.2f}\033[m')
else:
    print('\033[0:31mCódigo inválido!\033[m')
