"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

print('''
"uma string",
 "234",
 "a",
 "True",
 "42.3" ''')
 
 nome = 'Geek University'
print(nome, type(nome))

nome = "Gina's Bar"
print(nome, type(nome))

nome = 'Angelina \nJolie'
print(nome, type(nome))

nome = "Angelina \" Jolie"
print(nome, type(nome))

nome = 'Geek University'
print(nome.upper())

nome = 'Geek University'
print(nome.lower())

nome = 'geek university'
print(nome.title())

nome = 'Geek University'
print(nome.split())  # Transforma em uma lista de strings

nome = 'Felippe Andrade de Menezes'
print(f"Existem {len(nome.lower().split('e')) - 1} letra(s) 'e' em\n"
      f"{nome}")

print(nome[:4], nome[5:])  # Slice de string

# [   0,        1]
# ['Geek', 'University']
print(nome.split()[0], nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""","""42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1])  # Inversão da String Pythônico

print(nome.replace('e', 'i'))

print(type(nome))

# noinspection SpellCheckingInspection
texto = "socorram me subino onibus em marrocos"  # Palíndromo
print(texto)
print(texto[::-1])

nome = 'ana'  # Palíndromo
print(nome)
print(nome[::-1])
