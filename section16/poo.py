"""
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para modelos computacionais.

- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da POO:
    - Classe -> Modelo do objeto do mundo real sendo representado computacionalmente (modelo de dados);
    - Atributo -> Características do objeto (variáveis);
    - Método -> Comportamento do objeto (funções) e representam o que o objeto faz;
    - Construtor -> Método especial utilizado para criar os objetos (inicializar os atributos);
    - Objeto -> Instância da classe (exemplar da classe).

"""

numero = 10
print(numero, type(numero))

nome = 'Geek'
print(nome, type(nome))


class Produto:
    pass


ps4 = Produto()
print(ps4, type(ps4))
