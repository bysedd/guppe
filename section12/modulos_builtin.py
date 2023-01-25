"""
Trabalhando com Módulos Built-in (módulos integrados, que já vem instalados no Python)
________________________
/Python/Módulos builtin/
------------------------

# Utilizando apelidos para módulos
import random as rdn

r = rdn.random()
print(r)
while r < 0.99:
    r = rdn.random()
    print(r)

# Podemos importar todas as funções de um módulo utilizando o *
from random import *
print(random())

# Importando o módulo completo
import random
print(random.random())

# Utilizando apelidos para funções
from random import randint as rdi, randrange as rdr
print(rdi(5, 50))
print(rdr(5, 50, 5))

"""

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    choice
)

print(random())
print(randint(0, 9))
print(choice((13, 22)))
