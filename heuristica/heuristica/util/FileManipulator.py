import os

class FileManipulator:

  QUEBRA_DE_LINHA = '\n'

  def __init__(self, nome_do_arquivo):
    self.nome_do_arquivo = nome_do_arquivo
    self.processamentos = []
    self.janelas_iniciais = []
    self.janelas_finais = []
    self.configuracoes = []
    self.disponibilidades = []

    matriz = []

    # x = os.open('../test/' + nome_do_arquivo, flags = os.O_RDONLY)
    # caminho_arquivo = os.path.join(nome_do_arquivo)
    not_working = os.path.join('heuristica', 'test', 'instancia1.txt')
    working = 'C:\Aulas\Alunos\Python & R\Joice\Joice-Rodrigues\Joice-Rodrigues\heuristica\\test\\'
  
    working += nome_do_arquivo

    with open(working, 'r') as arquivo :
      count = 0
      for linha in arquivo.readlines():
        if linha == self.QUEBRA_DE_LINHA :
          matriz = self.__corrige__matriz__em__vetor__(matriz)
          self.__switch_case_atributo__(count, matriz)
          matriz = []
          count += 1 
          continue
        else :
          vetor = self.__linha_para_vetor__(linha)
          matriz.append(vetor)


  def __switch_case_atributo__(self, index, leitura):

    leitura = self.__corrige__matriz__em__vetor__(leitura)

    if index == 0:
      self.processamentos = leitura
    elif index == 1:
      self.janelas_iniciais = leitura
    elif index == 2:
      self.janelas_finais = leitura
    elif index == 3:
      self.configuracoes = leitura
    elif index == 4:
      self.disponibilidades = leitura



  def __linha_para_vetor__(self, linha):
    linha = linha.split()
  
    for index in range( len(linha) ):
      linha[index] = int( linha[index] )

    return linha

  def __corrige__matriz__em__vetor__(self, matriz) :
    if ( len(matriz) == 1 ) :
      aux = [ ]
      for elemento in matriz[0]:
        aux.append(elemento)
      return aux
    
    return matriz
  
  def __str__(self):
    aux =  f'Processamentos = {self.processamentos}\n'
    aux += f'Disponibilidades = {self.disponibilidades}\n'
    aux += f'Janelas Finais = {self.janelas_finais}\n'
    aux += f'Janelas Iniciais = {self.janelas_iniciais}\n'
    return aux
    