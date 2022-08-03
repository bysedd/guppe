"""
Loop while

Forma geral:

while expressão_booleana:
    // execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

# Exemplo 1:
num = 1
while num < 10:
    print(num)
    num += 1
# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2
resposta = ''
while not resposta.__contains__('sim'):
    resposta = input('Já acabou Jéssica? ').lower()

"""
