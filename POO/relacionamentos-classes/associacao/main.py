# Código baseado no vídeo do Otávio Miranda
# Nome:
# Associação - Python Orientado a Objetos - Aula 41
# Link:
# https://www.youtube.com/watch?v=lA4UAIEGKaU&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=7

from escritor import Escritor
from caneta import Caneta
from maquina_escrever import MaquinaEscrever


escritor =  Escritor('Joãozinho')
caneta = Caneta("Bic")
maquina = MaquinaEscrever()

# Uma classe não depende da outra para existir
# O Objeto recebe um objeto inteiro. É enviado o objeto inteiro
# Quando a ferramente é apagada a ferramenta continua existindo.
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
# só vai ser deleta quando não estiver mais associada a outra classe
# del caneta

print("------------")
del escritor
print("------------")
caneta.escrever()
maquina.escrever()

print("END------------------------")
