
import util.Filtro as Filtro

class FiltroDeEquipe(Filtro):

  def __init__(self, equipes):
    super().__init__(equipes)

  # ------------------------------------------
  
  def equipe_com_tempo_maior(self) -> Equipe:
    maior_tempo = super().equipes[0]

    for equipe in super().equipes:
      maior_tempo = max(equipe, maior_tempo)

    return maior_tempo  