from model.Maquina import Maquina

class Equipe:

  # construtor
  def __init__(self, id,  disponibilidade):
    self.id = id
    self.disponibilidade = disponibilidade
    self.maquinas = [ ]

  def adiciona_maquina(self, nova_maquina: Maquina):
    self.maquinas.append(nova_maquina)
  
  
