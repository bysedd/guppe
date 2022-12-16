"""
Decoradores (Decorators)

O que são decorators?
    São funções;
    Envolvem outras funções e aprimoram seus comportamentos;
    Também são exemplos de HOF;
    Tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

----------------------------------------
|          Function Decorator          |
----------------------------------------
    -------------------------------------
    |          Função Decorada          |
    -------------------------------------


# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo_educado():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um ótimo dia.')
    return sendo_educado()


def saudacao():
    print('Seja bem-vindo(a) à G.U.')


def raiva():
    print('EU TE ODEIO!')


# Testando 1
# saudacao()
seja_educado(saudacao)

# Testando 2
seja_educado(raiva)

# Decorators com Syntax Sugar (Açúcar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_educado_mesmo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um exelente dia.')
    return sendo_educado_mesmo


@seja_educado_mesmo
def se_apresentando():
    print(f'Meu nome é Felippe')


# Testando 1
se_apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


# Testando 2
dormir()

"""
'''
-----------------------------------------------
| Home | Serviços | Produtos | Administrativo |
-----------------------------------------------
OBS: É apenas um exemplo

site = https://www.suaempresa.com.br/
home_page = site + 'home'
services_page = site + 'services'
products_page = site + 'products'
admin_page = site + 'admin'


def check_login(request):
    if not request.user:
        redirect(site + 'login')


def home(request):
    return 'Pode acessar home'


def services(request):
    return 'Pode acessar serviços


def products(request):
    return 'Pode acessar produtos'


@check_login
def admin(request):
    return 'Pode acessar admin'
'''

# OBS: Não confunda Decorator com Decorator Function
