from model.Maquina import Maquina

class Equipe:

  # construtor
  def __init__(self, id,  disponibilidade, janela_final : list, janela_inicial : list ):
    self.id = id
    self.disponibilidade = disponibilidade
    self.janela_final = janela_final.copy()
    self.janela_inicial = janela_final.copy()
    self.maquinas = list[Maquina]

  def adiciona_maquina(self, nova_maquina: Maquina):
    self.maquinas.append(nova_maquina)
    self.__desconta_tempo_de_processamento__(nova_maquina)
    self.__desconta__tempo__disponibilidade__(nova_maquina)

  def tempo_de_processamento(self):
    soma = 0

    for maquina in self.maquinas:
       soma += maquina.tempo_de_processamento

    return soma

  def __desconta_tempo_de_processamento__(self, nova_maquina : Maquina):
    self.janela_final[nova_maquina.index] -= nova_maquina.tempo_processamento

  def __desconta__tempo__disponibilidade__(self, nova_maquina: Maquina):
    self.disponibilidade -= nova_maquina.tempo_processamento

  def __str__(self):
    aux = f'EQUIPE #{id:2.0}'
    aux += f'DISPONIBILIDADE: {self.disponibilidade}'
    aux += f'MAQUINAS:\n'
    aux += f'TEMPO TOTAL {self.tempo_de_processamento()}'

    for maquina in self.maquinas:
      aux += str(maquina) + '\n'

    return aux
