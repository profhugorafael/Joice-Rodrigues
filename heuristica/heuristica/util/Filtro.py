from model.Maquina import Maquina
from model.Equipe import Equipe

class Filtro:

  # ------------------------------------------

  def __init__(self, maquina : Maquina, equipes_disponiveis : list[Equipe]):
    self.maquina = maquina
    self.equipes_disponiveis = equipes_disponiveis.copy()

  # ------------------------------------------

  def filtraAtivosPorJanelaFinal(self):
    disponiveis_pos_filtro = [ ]

    for equipe in self.equipes_disponiveis:

      tempo_disponivel = equipe.janela_final[self.maquina.index]

      if tempo_disponivel >= self.maquina.tempo_processamento:
        disponiveis_pos_filtro.append(equipe)

    self.equipes_disponiveis = disponiveis_pos_filtro.copy()

  # ------------------------------------------
  
  def filtraAtivosPorDisponibilidade(self):
    disponiveis_pos_filtro = [ ]

    for equipe in self.equipes_disponiveis:
      if equipe.disponibilidade >= self.maquina.tempo_processamento:
        disponiveis_pos_filtro.append(equipe)

    self.equipes_disponiveis = disponiveis_pos_filtro.copy()

  # ------------------------------------------

  def ordenaPorJanelaFinal_desc(self) :
    ordenacao = sorted (
      list = self.equipes_disponiveis,
      key = lambda equipe : equipe.janela_final,
      reverse = True)

    self.equipes_disponiveis = ordenacao.copy()

  # ------------------------------------------

  def ordenaPorJanelaInicial_asc(self) : 
  
    ordenacao = sorted(
      list = self.equipes_disponiveis,
      key = lambda equipe : equipe.janela_inicial
    )

    self.equipes_disponiveis = ordenacao.copy()
