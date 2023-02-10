"""
O operador Walrus permite fazer a atribuição e retorno de um valor em uma única expressão.

variavel := expressão

nome = 'Geek University'
print(nome)

# Exemplo de função
print(nome := 'Geek University')

# <= Python 3.7
cesta = []
fruta = input('Informe a fruta: ').strip().lower()
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ').strip().lower()
print(f'Você comprou {len(cesta)} frutas')

"""

# >= Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ').strip().lower()) != 'jaca':
    cesta.append(fruta)
print(f'Você comprou {len(cesta)} frutas')
