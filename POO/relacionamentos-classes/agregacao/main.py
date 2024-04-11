# Código baseado no vídeo do Otávio Miranda
# Nome:
# Agregação - Python Orientado a Objetos - Aula 42
# Link:
# https://www.youtube.com/watch?v=ewGulRBQxOE&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=8

# Agregação é um tipo de associação, porém uma classe depende da outra para
# funcionar corretamente.
# O Carrinho de compras pode existir sem produtos, porém ele precisa deles
# para funcionar corretamente.
# Produto pode existir sozinho e não depende da classe CarrinhoDeCompras

# Outro exemplo:
# Um carro pode existir sem as rodas, porém não funciona direito.

from carrinho_compras import CarrinhoDeCompras
from produto import Produto

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)
carrinho = CarrinhoDeCompras()
carrinho2 = CarrinhoDeCompras()

carrinho.inserir_produto(p1, p2, p3, p1)
carrinho.lista_produtos()
print(carrinho.soma_total())

del carrinho

print()
carrinho2.inserir_produto(p1, p2, p3, p1)
carrinho2.lista_produtos()
print(carrinho2.soma_total())

print("FIM DA EXECUÇÃO ---------------")
