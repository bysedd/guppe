"""
Tipo None

O APAGAR dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém, falar que é um tipo sem tipo é mais apropriado.

OBS:
    — O tipo None é SEMPRE especificado com a primeira letra maiúscula.
    — O tipo None em Python é SEMPRE considerado como False

Certo: None
Errado: none

Quando utilizamos?

- Podemos utilizar None quando queremos enviar uma variável e inicializá-la com um tipo sem tipo, antes
de recebermos um valor final.
"""

numeros = None

print(numeros, type(numeros))

numeros = (1.44, 1.34, 5.67)
print(numeros, type(numeros))
