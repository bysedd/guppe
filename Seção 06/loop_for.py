"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C#
for(int i = 0; i < 10; i++) {
    //execução do loop
}

Python
for item in interavel:
    // execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range

range(valor_inicial, valor_final)

OBS: O valor final não é incluso.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), ...

for indice, letra in enumerate(nome):
    if letra == ' ':
        print()
    else:
        print(f'{letra}[{indice}]')

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline ( _ )

nome = 'Felippe Andrade de Menezes'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[0], valor[1])


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += numero
print(f'A soma total é \033[0:34m{soma}\033[m')

for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F60D, U+1F63C
# Modificado: U0001F60D, U0001F63C

_ = '\U0001F60D'
emoji = '\U0001F63C'

for _ in range(3):
    for num in range(1, 11):
        print(emoji * num)
"""
