"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

1 — SyntaxError ≥ Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que
o Python não reconhece como parte da linguagem.

Exemplos SyntaxError

a)
def funcao:
    print("Geek University")

b)
def = 1

c)
return

2 — NameError ≥ Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
print(geek)

b)
geek()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

b)
print("Geek" + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outra categoria de dado indexado utilizando
um índice inválido.

Exemplos IndexError

a)
lista = ["Geek"]
print(lista[02])

b)
lista = ["Geek"]
print(lista[0][10])

c)
tupla = ("Geek",)
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo correto,
mas valor inapropriado.

Exemplos com ValueError

a)
print(int("Geek"))

b)
print(float("Geek"))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dicionario = {"python": "university"}
print(dicionario["geek"])

7 - AttributeError ≥ Ocorre quando uma variável não tem um atributo/função.

Exemplos com AttributeError

a)
tupla = (11, 2, 31, 4)
tupla.sort()
print(tupla)

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
def nova():
print("Geek")

b)
for i in range(10):
print(i)

OBS: exceptions e Erros são sinônimos na programação.

OBS: importante ler e prestar atenção na saída de erro.
"""
