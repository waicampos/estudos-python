class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def __del__(self):
        print("Deletando Carrinho de Compras")

    def inserir_produto(self, *args):
        for produto in args:
            self.__produtos.append(produto)

    def lista_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        return total
