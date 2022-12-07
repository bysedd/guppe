from functions import error_message, print_formatado, confirm
from collections import OrderedDict


class Registros:
    def __init__(self):
        self.arquivo = OrderedDict()
        self.nome_arquivo = 'registros.csv'
        self.encoding = 'utf-8'
        self.moeda = 'R$'
        self.opcoes = {
            '1': 'Criar o arquivo de dados;',
            '2': 'Incluir um determinado registro no arquivo;',
            '3': 'Excluir um determinado vendedor no arquivo',
            '4': 'Alterar o valor de uma venda no arquivo;',
            '5': 'Imprimir os registros na saída padrão;',
            '6': 'Excluir o arquivo de dados;',
            '7': 'Finalizar o programa.'
        }

    def exibir_opcoes(self):
        print_formatado('Opções')
        [print(f'{k} - {v}') for k, v in self.opcoes.items()]

    def ler_arquivo(self):
        with open(self.nome_arquivo, encoding=self.encoding) as f:
            for linha in f.readlines():
                linha = linha.split('\n')[0].split(',')
                codigo, nome, vendas, mes = linha
                self.arquivo[int(codigo)] = {
                    'nome': nome.strip().title(),
                    'vendas': round(float(vendas), 2),
                    'mes': int(mes)
                }

    def criar_arquivo(self):
        import os
        if not os.path.isfile(self.nome_arquivo):
            f = open(self.nome_arquivo, 'w', encoding=self.encoding)
            f.close()
            print_formatado(f"Arquivo '{self.nome_arquivo}' criado")
        else:
            print(error_message('O arquivo já existe'))

    def adicionar_registro(self, d: dict = None):
        if not d:
            continuar = True
            while continuar:
                try:
                    print_formatado('Adicionar registro')
                    codigo_vendedor = int(input('Código da venda: '))
                    if codigo_vendedor <= 0:
                        print(error_message('Código inválido'))
                        continue
                    nome_vendedor = input('Nome do vendedor: ').strip().title()

                    if not nome_vendedor.isalpha():
                        print(error_message('Nome inválido'))
                        continue
                    valor_da_venda = float(input(f'Valor da venda: {self.moeda}'))

                    mes = int(input('Número do mês: '))
                    if not 1 <= mes <= 12:
                        print(error_message('Mês inválido'))
                        continue
                    self.arquivo[codigo_vendedor] = {
                        'nome': nome_vendedor,
                        'vendas': valor_da_venda,
                        'mes': mes
                    }
                except ValueError as err:
                    print(error_message(err))
                finally:
                    continuar = confirm('Quer adicionar mais registro (y/n)? ')
        else:
            self.arquivo = d.copy()
        with open(self.nome_arquivo, 'w', encoding=self.encoding) as f:
            for k, v in self.arquivo.items():
                f.write(f"{k},{v['nome']},{v['vendas']},{v['mes']}\n")

    def excluir_vendedor(self):
        continuar = True
        arquivo = self.arquivo.copy()

        while continuar:
            print_formatado('Excluir determinado vendedor')
            self.ler_arquivo()
            find = False
            nome_vendedor = input('Digite o nome do vendedor: ').strip().title()
            for k, v in arquivo.items():
                if v['nome'] == nome_vendedor:
                    self.arquivo.pop(k)
                    find = True
            if not find:
                print(error_message('Nome do vendedor não encontrado'))
            continuar = confirm('Quer continuar (y/n)? ')

        if arquivo:
            self.adicionar_registro(self.arquivo)

    def alterar_vendas(self):
        """Alterar o valor de uma venda no arquivo"""
        continuar = True
        arquivo = self.arquivo.copy()

        while continuar:
            try:
                print_formatado('Alterar o valor de uma venda')
                self.ler_arquivo()
                find = False
                codigo_venda = int(input('Digite o código da venda: '))

                for k, v in arquivo.items():
                    if k == codigo_venda:
                        print_formatado(f"{k} | {v['nome']} | {v['vendas']} | {v['mes']}")
                        novo_valor = float(input(f'Digite um novo valor para atribuir a esta venda: {self.moeda}'))
                        self.arquivo[k]['vendas'] = round(novo_valor, 2)
                        find = True
                if not find:
                    print(error_message('Código da venda não encontrado'))
                continuar = confirm('Quer continuar (y/n)? ')
            except ValueError:
                print(error_message('Código inválido'))
        self.adicionar_registro(self.arquivo)

    def excluir_arquivo(self):
        import os
        print_formatado('Excluir arquivo de dados')
        confirmar = confirm('Você que tem certeza disso (y/n)? ')
        if confirmar:
            os.remove(self.nome_arquivo)

    def imprimir_registros(self):
        import calendar

        self.ler_arquivo()
        arquivo_ordenado = sorted(self.arquivo.items(), key=lambda item: item[1]['mes'])

        print_formatado('Registros')
        for k, v in arquivo_ordenado:
            print(f"{k} | {v['nome']} | {v['vendas']} | {calendar.month_name[v['mes']].lower()}".center(80))


registros = Registros()

while True:
    registros.exibir_opcoes()
    opt = input('Escolha uma opção: ')
    match opt:
        case '1':
            registros.criar_arquivo()
        case '2':
            registros.adicionar_registro()
        case '3':
            registros.excluir_vendedor()
        case '4':
            registros.alterar_vendas()
        case '5':
            registros.imprimir_registros()
        case '6':
            registros.excluir_arquivo()
        case '7':
            print_formatado('Programa finalizado')
            break
        case _:
            print(error_message('Opção inválida'))
