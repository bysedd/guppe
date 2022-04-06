"""
Recebendo dados do usuário

input() -> Qualquer dado recebido via input é do tipo str

Em Python string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""
from datetime import date

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % name)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}".format(name))

# Exemplo de print 'mais atual' +3.7
print(f"Seja bem-vinda {nome}")

# print("Qual sua idade? ")
# idade = int(input())

idade = int(input("Qual sua idade? "))

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x
# print("O(A) %s tem anos %s" % (name, idade))

# Exemplo de print 'moderno' 3.x
print(f"A {nome} tem {idade} anos")

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f"A {nome} nasceu em {date.today().year - idade}")
