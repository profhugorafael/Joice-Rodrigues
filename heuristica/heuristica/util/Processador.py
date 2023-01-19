from util.FileManipulator import FileManipulator
from util.Filtro import Filtro
from model.Equipe import Equipe
from model.Maquina import Maquina

def eh_equipe(elemento):
  return True if isinstance(elemento, Equipe) else False

class Processador:

  def __init__(self, dados: FileManipulator):
    self.dados = dados
    self.equipes = []
    self.index = 0
    self.__soma_atual__ = 1
    quantidade_equipes = len(self.dados.configuracoes[0])
    self.__checklist_configuracoes__ = [ ]
    self.limit = quantidade_equipes

    for _ in range(len(self.dados.configuracoes) + 1):
      self.__checklist_configuracoes__.append(False)

  # ------------------------------------------

  def inicializar_equipes(self) :    
    quantidade = len(self.dados.configuracoes[0])

    for i in range(quantidade):
      equipe = Equipe(
        id = i,
        disponibilidade = self.dados.disponibilidades[i],
        janela_final = self.dados.janelas_finais,
        janela_inicial = self.dados.janelas_iniciais
      )

      if eh_equipe(equipe) : self.equipes.append(equipe)

  # ------------------------------------------

  def processar_proximo(self) -> bool :
    
    # ! loop infinito com o próximo index
    
    self.index = self.__proximo_index__()

    if self.__alcancou_limite__(): 
      return False

    configuracao = self.dados.configuracoes[self.index]
    equipes_disponiveis = self.__captura_equipes_disponiveis__(configuracao)
    self.__distribui_para_equipes_disponiveis__(equipes_disponiveis)

    self.index += 1
    return True

  # ------------------------------------------

  def __distribui_para_equipes_disponiveis__(self, equipes_disponiveis):

    processamento = self.dados.processamentos[self.index]

    for index_maquina in range( len(processamento) ):

      maquina = Maquina(
        tempo_processamento = processamento[index_maquina],
        index_maquina = index_maquina,
        indice_atividade = self.index
      )

      filtro = Filtro(maquina, equipes_disponiveis)

      filtro.filtraAtivosPorJanelaFinal()
      filtro.filtraAtivosPorDisponibilidade()
      filtro.ordenaPorJanelaFinal_desc()
      filtro.ordenaPorJanelaInicial_asc()

      assert len(filtro.equipes_disponiveis) > 0, 'problema nos filtros'

      indice_para_receber = filtro.equipes_disponiveis[0].id
      self.equipes[indice_para_receber].adiciona_maquina(maquina)

  # ------------------------------------------

  def __captura_equipes_disponiveis__(self, configuracao):
    disponiveis = [ ]

    for i in range( len(configuracao) ):
      if configuracao[i] : 
        equipe = self.equipes[i]
        if eh_equipe(equipe) :
          disponiveis.append(equipe)
    
    return disponiveis

  # ------------------------------------------

  def __str__(self):
    aux = ''

    for equipe in self.equipes:
      aux += str(equipe) + '\n'
      aux += '---------------\n'

    return aux

  # ------------------------------------------

  def __proximo_index__(self):

    for i in range(len(self.dados.configuracoes)):
      configuracao = self.dados.configuracoes[i]
      soma = sum(configuracao)
      nao_processada = self.__checklist_configuracoes__[i]

      if soma == self.__soma_atual__ and nao_processada:
        self.__checklist_configuracoes__[i] = True
        return i

    self.__soma_atual__ += 1
    if not self.__alcancou_limite__():
      return self.__proximo_index__() 


  # ------------------------------------------
  
  def __alcancou_limite__(self) -> bool :

    if self.index > self.limit : 
      return True

    return False