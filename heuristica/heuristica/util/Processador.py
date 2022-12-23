from util.FileManipulator import FileManipulator
from util.Filtro import Filtro
from model.Equipe import Equipe
from model.Maquina import Maquina

class Processador:

  def __init__(self, dados : FileManipulator, equipes: list[Equipe] ):
    self.dados = dados
    self.equipes = equipes
    self.index = 0
    self.limit = len(self.dados.processamentos)
    print(self.limit)

  # ------------------------------------------

  def inicializar_equipes(self):
    
    quantidade = len(self.dados.configuracoes[0])

    for i in range(quantidade):
      equipe = Equipe(
        id = i,
        disponibilidade = self.dados.disponibilidades[i],
        janela_final = self.dados.janelas_finais,
        janela_inicial = self.dados.janelas_iniciais
      )

      self.equipes().append(equipe)

  # ------------------------------------------

  def processar_proximo(self):
    if self.index >= self.limit : 
      print('its over')
      return False

    configuracao = self.dados.configuracoes[self.index]
    equipes_disponiveis = self.__captura_equipes_disponiveis__(configuracao)
    self.__distribui_para_equipes_disponiveis__(equipes_disponiveis)
    self.index += 1
    return True

  # ------------------------------------------

  def __distribui_para_equipes_disponiveis__(self, equipes_disponiveis : list[Equipe]):
    processamento = self.dados.processamentos[self.index]

    for index_maquina in range( len(processamento) ):

      maquina = Maquina(
        tempo_processamento = processamento[index_maquina],
        index_maquina = index_maquina,
        indice_atividade = self.index
      )

      filtro = Filtro(
        equipes_disponiveis = equipes_disponiveis,
        maquina = maquina
      )

      filtro.filtraAtivosPorJanelaFinal()
      filtro.filtraAtivosPorDisponibilidade()
      filtro.ordenaPorJanelaFinal_desc()
      filtro.ordenaPorJanelaInicial_asc()

      assert len(filtro.equipes_disponiveis) > 0, 'problema nos filtros'

      index = filtro.equipes_disponiveis[0].id
      equipes_disponiveis[index].adiciona_maquina(maquina)

  # ------------------------------------------

  def __captura_equipes_disponiveis__(self, configuracao):
    disponiveis = list[Equipe]

    for i in range( len(configuracao) ):
      if configuracao[i] : 
        print(i)
        equipe = list(self.equipes)[i]
        disponiveis().append(equipe)
    
    return disponiveis

  # ------------------------------------------

  def __str__(self):
    aux = ''

    for equipe in self.equipes:
      aux += str(equipe) + '\n'
      aux += '---------------\n'

    return aux