"""
Definindo Funções

— Funções são pequenas partes de código que realizam tarefas específicas;
— Pode ou não receber entradas de dados e retornar uma saída de dados;
— Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: se você escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muitas outras;
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

curso = 'Programação em Python: Essencial'

cores.append('roxo')

cores.clear()

# DRY — Don't Repeat Yourself — Não repita você mesmo / Não repita seu código.

# Mas, como definir funções?

"""
Em Python, a forma geral de definir uma função é:


def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao


Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (snake_case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste
                   bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
     uma função. Também abrimos o bloco de código com o dois pontos : que é utilizado em Python para definir blocos.
"""


# Definindo a primeira função:


def diz_oi():
    """
    Função que diz 'Oi!'
    """
    print('Oi!')


"""
OBS:

1 - Dentro das nossas funções podemos utilizar outras funções;
2 - Nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Esta função não recebe nenhum parâmetro de entrada;
4 - Não retorna nada.
"""

# Utilizando funções
diz_oi()

"""
ATENÇÃO

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi
diz_oi ()

# Certo!
diz_oi()
"""


# Exemplo 2


def cantar_parabens():
    """
    Função que canta parabéns
    """
    print('''Parabéns pra você
Nesta data querida
Muitas felicidades
Muitos anos de vida''')


# for _ in range(4):
#    cantar_parabens()

# Em Python, podemos criar variáveis da função e executar esta função através da variável.

canta = cantar_parabens

canta()
