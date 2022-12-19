class Maquina:

  def __init__(self, tempo_processamento, indice_atividade, index_maquina):
     self.tempo_processamento = tempo_processamento
     self.atividade = indice_atividade
     self.index = index_maquina

  def description(self) :
    print('my description')

  def __str__(self):
    return f'tempo de processamento {self.tempo_processamento} | indice atividade : {self.atividade} | maquina de origem : {self.index}'