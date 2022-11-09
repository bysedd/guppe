"""
Módulo random e o que são módulos?

* Em Python, módulos nada mais são do que outros arquivos Python

Módulo Random ≥ Possui várias funções para geração de número pseudo-aleatórios.

# OBS: existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando o módulo completo (não recomendado).
import random

# random() -> Gera um número real pseudo-aleatório entre 0 e 1.

# OBS: ao realizar o import do módulo completo, todas as funções, atributos, classes e propriedades que estiverem
# no módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() o pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função no módulo random.

# Forma 2 - Importando uma função específica do módulo (forma recomendada)
from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

[print(random()) for _ in range(10)]

# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos.

from random import uniform

[print(uniform(5, 10)) for _ in range(10)] # O 10 não é incluído.

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
[print(randint(1, 60), end=" ") for _ in range(6)]  # começa em 1 e vai até 60

# choice() -> Mostre um valor aleatório entre um iterável.
from random import choice

jogadas = ("pedra", "papel", "tesoura")

print(choice(jogadas), choice(jogadas), sep=" x ")

"""

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ["K", "Q", "J", "A", "2", "3", "4", "5", "6", "7"]

print(cartas)
shuffle(cartas)
print(cartas.pop())
