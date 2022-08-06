'''
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se persarmos em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se pensarmos em uma função, já sabemos que temos funções que:
- não possuem entrada;
- não possuem saída;
- possuem entrada mas não possuem saída;
- não possuem entrada mas possuem saída;
- possuem entrada e saída.
'''


def quadrado(numero: int):
    """
    Função que retorna o x²
    :param numero: Número que será elevado ao quadrado
    :return: numero ** 2
    """
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))


def cantar_parabens(aniversariante: str):
    """
    Função que canta parabéns
    :param aniversariante: Nome do aniversariante
    :return: None
    """
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o(a) {aniversariante}')


cantar_parabens('Felippe')


# Funções podem ter 'n' parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo


def soma(a: float, b: float):
    """
    Função que soma dois números
    :param a: Primeiro número
    :param b: Segundo número
    :return: a + b    
    """
    return a + b


def multiplica(num1: float, num2: float):
    """
    Função que multiplica dois números
    :param num1: Primeiro número
    :param num2: Segundo número
    :return: num1 * num2
    """
    return num1 * num2


def outra(num1: float, b: float, msg: str):
    """
    Função que repete uma mensagem
    :param num1: Número que será acrescentado a soma
    :param b: Número que será somado
    :param msg: Mensagem que será repetida
    :return: (num1 + b) * msg
    """
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20), end='\n\n')

print(multiplica(4, 5))
print(multiplica(2, 8), end='\n\n')

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))


# OBS: se informarmos um número errado de parâmetro ou argumentos, teremos TypeError


def nome_completo(nome: str, sobrenome: str):
    """
    Função que exibe o nome completo
    :param nome: Nome
    :param sobrenome: Sobrenome
    :return: Nome completo.
    """
    nome = nome.strip()
    sobrenome = sobrenome.strip()
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Felippe', 'Andrade'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função.

# A ordem dos parâmetros importa!

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina   ', sobrenome='Jolie'))

from typing import Collection


def soma_impares(numeros: Collection):
    """
    Função que soma todos os números ímpares dentro de uma coleção.
    :param numeros: Coleção de números
    :return: Total
    """
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


print(soma_impares([1, 2, 3, 4, 5, 6, 7]))
print(soma_impares((8, 9, 10, 11, 12, 13, 14)))
print(soma_impares(3))
