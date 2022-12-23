from model.Maquina import Maquina
from model.Equipe import Equipe
from util.Processador import Processador
from util.FileManipulator import FileManipulator

dados = FileManipulator('instancia1.txt')
equipes = list[Equipe]

processador = Processador(
  equipes = equipes,
  dados = dados)

processador.inicializar_equipes()

while processador.processar_proximo() :
  print(f' --- index = {processador.index}')

print(processador)