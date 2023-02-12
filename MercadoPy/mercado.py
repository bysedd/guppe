from typing import List, Dict
from time import sleep
import pickle
import os

from utils import helper
from models.produto import Produto


class Mercado:
    produtos: List[Produto] = []
    carrinho: List[Dict[Produto, int]] = []
    tracos: str = '=' * 50
    ARQUIVO: str = './data/produtos.txt'

    def __init__(self) -> None:
        if os.path.exists(Mercado.ARQUIVO):
            with open(Mercado.ARQUIVO, 'rb') as f:
                try:
                    Mercado.produtos = pickle.load(f)
                except EOFError:
                    print('Arquivo vazio.')
                    print(Mercado.tracos)
        else:
            with open(Mercado.ARQUIVO, 'wb'):
                pass

    @classmethod
    def menu(cls) -> None:
        print('1 - Cadastrar produto')
        print('2 - Listar produtos')
        print('3 - Comprar produto')
        print('4 - Visualizar carrinho')
        print('5 - Fechar pedido')
        print('6 - Sair do sistema')
        print(cls.tracos)

        opcao: int = int(input('Digite uma opção: '))

        match opcao:
            case 1:
                Mercado.cadastrar_produto()
            case 2:
                Mercado.listar_produtos()
            case 3:
                Mercado.comprar_produto()
            case 4:
                Mercado.visualizar_carrinho()
            case 5:
                Mercado.fechar_pedido()
            case 6:
                raise SystemExit('Saindo do sistema...')
            case _:
                print('Opção inválida.')
                sleep(1)

    @classmethod
    def cadastrar_produto(cls):
        print(cls.tracos)
        print('CADASTRO DE PRODUTOS'.center(50))
        print(cls.tracos)

        # Recebe os dados do produto a ser cadastrado e cria um objeto
        codigo: int = len(cls.produtos) + 1
        nome: str = input('Nome do produto: ').strip().title()
        preco: float = float(input('Preço: '))
        produto: Produto = Produto(codigo, nome, preco)

        # Adiciona o produto na lista de produtos
        cls.produtos.append(produto)

        # Salva a lista de produtos no arquivo
        with open(cls.ARQUIVO, 'wb') as f:
            pickle.dump(cls.produtos, f)
        print(f'Produto {produto.nome} cadastrado com sucesso.')
        print(Mercado.tracos)
        sleep(1)

    @classmethod
    def listar_produtos(cls) -> None:
        print(cls.tracos)
        print('LISTAGEM DE PRODUTOS'.center(50))
        print(cls.tracos)

        # Verifica se há produtos cadastrados
        if len(cls.produtos) == 0:
            print('Não há produtos cadastrados.')
            print(cls.tracos)
            sleep(1)
        # Se houver, lista os produtos
        else:
            for produto in cls.produtos:
                print(produto)
                print(cls.tracos)
                sleep(1)

    @classmethod
    def comprar_produto(cls) -> None:
        if len(cls.produtos) == 0:
            print('Não há produtos cadastrados.')
            print(cls.tracos)
            sleep(1)
        else:
            # Lista os produtos cadastrados
            cls.listar_produtos()

            # Recebe o código do produto que o usuário deseja adicionar ao carrinho
            codigo: int = int(input('Digite o "id" do produto que deseja adicionar ao carrinho: '))

            # Busca o produto pelo código
            produto: Produto = cls._pega_produto_codigo(codigo)
            if produto:
                quantidade: int = int(input('Digite a quantidade: '))
                if quantidade > 0:
                    cls.carrinho.append({produto: quantidade})
                    print(f'{quantidade}x {produto.nome} adicionado ao carrinho.')
                    print(cls.tracos)
                    sleep(1)
                else:
                    print('Quantidade inválida.')
                    print(cls.tracos)
                    sleep(1)
            else:
                print('Produto não encontrado.')
                print(cls.tracos)
                sleep(1)

    @classmethod
    def visualizar_carrinho(cls):
        if not cls.carrinho:
            print('Carrinho vazio.')
            print(cls.tracos)
            sleep(1)
        else:
            print(cls.tracos)
            print('CARRINHO'.center(50))
            print(cls.tracos)

            # Calcula o total do pedido
            print(f'{cls.tracos}\nTotal: {helper.formata_moeda(cls._calcula_total())}')
            print(cls.tracos)
            sleep(1)

    @classmethod
    def fechar_pedido(cls) -> None:
        if not cls.carrinho:
            print('Carrinho vazio.')
            print(cls.tracos)
            sleep(1)
            return
        else:
            print(cls.tracos)
            print('RESUMO DO PEDIDO'.center(50))
            print(cls.tracos)

            # Calcula o total do pedido
            print(f'{cls.tracos}\nTotal: {helper.formata_moeda(cls._calcula_total())}')
            print(cls.tracos)
            sleep(1)

            # Confirma o pedido
            while True:
                opcao: str = input('Confirma o pedido? [S/N] ').strip().upper()[0]
                if opcao in 'SN':
                    break
                print('Opção inválida.')
                sleep(1)

            # Se confirmado, exibe mensagem de pedido confirmado e limpa o carrinho
            if opcao == 'S':
                print('Pedido confirmado. Volte sempre!')
                cls.carrinho.clear()
                sleep(2)
            # Se não confirmado, exibe mensagem de pedido cancelado
            else:
                print('Pedido cancelado.')
                sleep(1)
            print(cls.tracos)

    @classmethod
    def _pega_produto_codigo(cls, codigo: int, /) -> Produto:
        """
        Retorna o produto com o código informado ou None se não encontrar.
        :param codigo: O código do produto a ser buscado.
        :return:
        """
        for produto in cls.produtos:
            if produto.id == codigo:
                return produto

    @classmethod
    def _calcula_total(cls) -> float:
        """
        Calcula o total do pedido e exibe o resumo do pedido.
        :return: O total do pedido.
        """
        total: float = 0
        for item in cls.carrinho:
            for dados in item.items():
                # dados é uma tupla com o produto e a quantidade
                produto, quantidade = dados
                subtotal: float = produto.preco * quantidade
                total += subtotal
                print(f'{produto.nome} - {quantidade}x - {helper.formata_moeda(subtotal)}')
                sleep(1)
        return total
