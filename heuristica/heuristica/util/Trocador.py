
import util.Filtro as Filtro
import model.Maquina as Maquina

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

  # ------------------------------------------

  def captura_equipes_disponiveis(self, maquina):
    disponiveis = []
    
    for equipe in self.equipes():
      if equipe.disponibilidade > maquina.tempo_processamento:
        disponiveis.append(equipe)

    return disponiveis

  # ------------------------------------------

  def pior_maquina_da_equipe(self, equipe):
    pior_maquina = equipe.maquinas[0]

    for maquina in equipe.maquinas:
      if maquina.tempo_de_processamento > pior_maquina.tempo_de_processamento:
        pior_maquina = maquina

    return pior_maquina

  # ------------------------------------------