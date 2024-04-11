# Código baseado no vídeo do Otávio Miranda
# Nome:
# Composição - Python Orientado a Objetos - Aula 43
# Link:
# https://www.youtube.com/watch?v=O6F77N09HdI&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=9

# Composição é a relação mais forte entre classes. Uma classe vai ser dona de objetos de outra classe.
# Se a classe principal for apagada, todos os objetos que a classe utilizou serão apagados com ela.

from cliente import Cliente

c1 = Cliente('Paulo', 36)
c1.insere_enderecos('Florianópolis', 'Santa Catarina')
c1.insere_enderecos('Curitiba', 'Paraná')
c1.lista_enderecos()

del c1

print()
c2 = Cliente('Maria', 21)
c2.insere_enderecos('São Paulo', 'São Paulo')
c2.insere_enderecos('Recife', 'Pernambuco')
c2.lista_enderecos()

print("FIM DA EXECUÇÃO-----------------------------")
