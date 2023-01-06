from model.Maquina import Maquina
from model.Equipe import Equipe
from util.Processador import Processador
from util.FileManipulator import FileManipulator

dados = FileManipulator('instancia1.txt')

processador = Processador(dados)
processador.inicializar_equipes()

while processador.processar_proximo() :
  print(f' --- index = {processador.index}')

print(processador)