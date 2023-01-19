from model.Maquina import Maquina
from model.Equipe import Equipe
from util.Processador import Processador
from util.FileManipulator import FileManipulator

dados = FileManipulator('instancia11.txt')

processador = Processador(dados)
processador.inicializar_equipes()

while processador.processar_proximo() :
  pass

print(processador)