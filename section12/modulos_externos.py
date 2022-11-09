"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado 'pip' - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo no terminal:
pip install nome_do_modulo

Instalando o pacote colorama:
pip install colorama

Utilizando o pacote instalado

from colorama import init, Fore
init()

print(Fore.MAGENTA + "Geek University")
print(Fore.BLUE + "Geek University")
"""

import pydf

pdf = pydf.generate_pdf("<h1>Geek University</h1>"
                        "<br/>"
                        "<br/>"
                        "<strong>Programa&ccedil;&atilde;o em Python: Essencial</strong")

with open("test_doc_pdf", "wb") as f:
    f.write(pdf)
