"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;
Pacote -> É um diretório contendo uma coleção de módulos;

OBS: nas versões 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py
    Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas
    normalmente ainda é utilizado para manter compatibilidade.

from geek import (geek1, geek2)
from geek.university import (geek3, geek4)

print(geek1.soma(4, 6))

print(geek1.PI)

print(geek2.CURSO)

print(geek3.retorno1(), geek4.retorno2())
"""

from geek.geek1 import soma
from geek.university.geek3 import retorno1

print(soma(6, 9))
print(retorno1().lower() + "university.com.br")
