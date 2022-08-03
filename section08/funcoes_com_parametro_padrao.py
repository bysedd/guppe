"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
	return numero ** 2
print(quadrado(3))
print(quadrado())  # TypeError


def exponencial(numero=4, potencia=2):
	return numero ** potencia
print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro 'numero', e será calculado o quadrado deste número:
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro 'numero' e o segundo ao parâmetro 'potencia'. Então será calculada esta potência.

print(exponencial())

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# others exemplos
def soma(num1=5, num2=3):
	return num1 + num2
print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo
def mostra_informacao(nome: str='Geek', instrutor: bool=False):
	if nome == 'Geek' and instrutor:
		return 'Bem vindo instrutor Geek!'
	elif nome == 'Geek':
		return 'Eu pensei que você era o instrutor'
	return f'Olá {nome}'
print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Bolsonaro'))


Por quê utilizar parâmetros com valor default?
	- Nos permite ser mais flexíveis nas funções;
	- Evita erros com parâmetros incorretos;
	- Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilizar como valores default para parâmetros?
	- Qualquer tipo de dado:
		- int, str, float, bool, list, tuple, dict, def, etc...

# Exemplos
def soma(num1: float, num2: float):
	return num1 + num2

def subtracao(num1: float, num2: float):
	return num1 - num2

def mat(num1, num2, function=soma):
	return function(num1, num2)

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # global

def diz_oi():
	instrutor = 'Python'  # local
	return f'Oi {instrutor}'

print(diz_oi())

# OBS: se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
	prof = 'Geek'
	return f'Olá {prof}'

print(diz_oi())
print(prof)  # NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
	total += 1  # UnboundLocalError (A variável está sendo utilizada para processamento sem ter sido inicializada)
	return total

print(incrementa())

total = 0

def incrementa():
	global total  # Avisando que queremos utilizar a variável global
	total += 1
	return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também existe uma forma especial de escopo de variável (incomum)

def fora():
	contador = 0

	def dentro():
		nonlocal contador
		contador += 1
		return contador
	return dentro()

print(fora())
print(fora())
print(fora())

"""
