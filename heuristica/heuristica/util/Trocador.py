
import util.Filtro as Filtro
import model.Maquina as Maquina
from random import randint as posicao_aleatoria

class Trocador:

  def __init__(self, equipes, configuracoes):
    self.configuracoes = configuracoes
    self.equipes = equipes
    self.equipes_ordenadas = sorted(equipes, key=lambda x: x.disponibilidade)

  # [ 12, 14, 15, 20 ]
  #    ^  ^      
  # ORDENAÇÃO: n*log(n)
  # COMPLEXIDADE: (n)(n-1)(n*log(n))/2
  # IDENTIFICAR: condição de parada
  # PROBLEMA: loop de trocas
  # Ordena e captura disponiveis por disponibilidade e configuração

  # maquina -> origem == ind. ativ -> config

  # ------------------------------------------

  def realiza_troca(self):
    self.ordena_equipes_por_disponibilidade()
    equipe_origem = self.equipes[0]
    maquina = self.pior_maquina_da_equipe(equipe_origem)
    disponiveis = self.equipes_disponiveis(maquina)

    if len(disponiveis) == 0:
      return
      
    pos_equipe_destino = posicao_aleatoria(0, len(disponiveis) - 1)
    equipe_destino = disponiveis[pos_equipe_destino]

    equipe_origem.maquinas.remove(maquina)
    equipe_destino.maquinas.append(maquina)

  # ------------------------------------------

  def equipes_disponiveis(self, maquina):

    disponiveis_por_disponibilidade = self.captura_equipes_com_disponibilidade(maquina)
    disponiveis_por_configuracao = self.captura_equipes_por_configuracao(maquina)

    comum = lambda element: element in disponiveis_por_disponibilidade
    interseccao = list(filter(comum, disponiveis_por_configuracao))

    return interseccao

  # ------------------------------------------

  def captura_equipes_com_disponibilidade(self, maquina):
    disponiveis = []
    configuracao = self.configuracoes[maquina.atividade]
      
    for i in range(len(configuracao)):
      valor = configuracao[i]

      if valor == 1:
        disponiveis.append(self.equipes[i])

    return disponiveis

  # ------------------------------------------

  def captura_equipes_por_configuracao(self, maquina):
    disponiveis = []
      
    for equipe in self.equipes():
      if equipe.disponibilidade > maquina.tempo_processamento:
        disponiveis.append(equipe)

    return disponiveis

  # ------------------------------------------

  def ordena_equipes_por_disponibilidade(self):
    criterio_por_disponibilidade = lambda equipe: equipe.disponibilidade
    # ! TODO checar se a melhor ordem realmente é a reversed
    return sorted(self.equipes, criterio_por_disponibilidade, reverse = True)

  # ------------------------------------------

  def pior_maquina_da_equipe(self, equipe):
    pior_maquina = equipe.maquinas[0]

    for maquina in equipe.maquinas:
      if maquina.tempo_de_processamento > pior_maquina.tempo_de_processamento:
        pior_maquina = maquina

    return pior_maquina

  # ------------------------------------------