def get_idade(data_de_nascimento: str = "01/06/2005"):
    """
    Converte a data de nascimento em idade (anos)
    :param data_de_nascimento: Deve ter o seguinte formato: dia/mes/ano
    :return: Retorna a idade
    """
    from datetime import date
    dia, mes, ano = data_de_nascimento.split("/")
    return (date.today() - date(day=int(dia), month=int(mes), year=int(ano))).days // 365


def str_to_bin(string: str = "Hello World!"):
    """
    Converte um tipo em outro.
    :param string: string
    :return: binário
    """
    binario = ""
    for i in string:
        binario += bin(ord(i))[2::]
    return binario


def float_to_bin(decimal: float = 7):
    """
    Convete um número flutuante para um binário.
    :param decimal: número com ponto flutuante
    :return: binário
    """
    decimal = str(decimal).split(".")
    binario = ""
    for numero in decimal:
        binario += f"{bin(int(numero))}"
        if "0b" in binario:
            binario = binario.replace("0b", "")
    return binario


def error_message(mensagem: (str, TypeError), br=False):
    """
    Formata uma mensagem de erro
    :param mensagem: Mensagem
    :param br: Quebrar linha
    :return: Mensagem formatada
    """
    from colorama import Fore, Style
    break_line = "\n"
    string = f"{Fore.RED}{mensagem}{Style.RESET_ALL}"
    return string + break_line if br else string


def print_formatado(mensagem: str, detalhe: str = "-=", qtd: int = 40):
    """
    Impressão customizada
    :param mensagem: Mensagem
    :param detalhe: Detalhe para colocar em cima e em baixo da mensagem
    :param qtd: Quantidade de detalhes (tamanho)
    :return: None
    """
    len_d = len(detalhe)
    print(f"{detalhe * qtd}\n"
          f"{mensagem.center(len_d * qtd)}\n"
          f"{detalhe * qtd}")


def confirm(message):
    """
    Fica a perguntar até escolher entre 'sim' ou 'não'.
    :param message: Mensagem
    :return: Retorna True se você responder 'sim' ou False se responder 'não'
    """
    sair = input(message).strip().lower()
    while sair not in ("y", "n"):
        sair = input(message).strip().lower()
    return True if sair == "y" else False
