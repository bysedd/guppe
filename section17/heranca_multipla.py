"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo
com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas formas:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class MultiDerivada(Base6):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
 os atributos e métodos de todas as classes herdadas.


"""
