import model.Equipe as Equipe

from util.Processador import Processador
from util.FileManipulator import FileManipulator
from cmath import exp as complex_exp
from random import uniform as uniform_random

def exp(number):
  return complex_exp(number).real

dados = FileManipulator('instancia3.txt')

processador = Processador(dados)
processador.inicializar_equipes()

while processador.processar_proximo() :
  pass

print(processador)
# maiores -> menores -> realoca
# critério (energia/função objetivo) -> equipe.tempo_de_processamento
# 

def initial_solution() :
  dados = FileManipulator('instancia3.txt')
  processador = Processador(dados)
  processador.inicializar_equipes()
  while processador.processar_proximo() :
    continue
  
  return processador.equipes

def generate_neighbor(equipes):
  alternative_solution = equipes

  

def energy(equipe):
  if not isinstance(equipe, Equipe):
    pass

  return equipe.tempo_de_processamento

def simulated_annealing(temperature, cooling_rate, max_iterations):
    # machines: lista de máquinas
    # es
    # temperature: temperatura iniciateams: lista de equipl
    # cooling_rate: taxa de resfriamento
    # max_iterations: número máximo de iterações

    # Inicializa a solução atual com uma distribuição aleatória de máquinas em equipes
    current_solution = initial_solution()
    best_solution = current_solution

    # Loop principal
    for i in range(max_iterations):
        # Gera uma nova solução a partir da solução atual
        new_solution = generate_neighbor(current_solution)

        # Calcula a diferença de energia entre a nova solução e a solução atual
        energy_delta = energy(new_solution) - energy(current_solution)

        # Se a nova solução é melhor, aceita-a como a solução atual
        if energy_delta < 0:
            current_solution = new_solution
            # Atualiza a melhor solução se a nova solução for ainda melhor
            if energy(new_solution) < energy(best_solution):
                best_solution = new_solution
        else:
            # Senão, aceita a nova solução com uma probabilidade determinada pela temperatura
            p = uniform_random(0, 1)
            if p < exp(-energy_delta / temperature):
                current_solution = new_solution

        # Reduz a temperatura
        temperature = temperature * cooling_rate

    return best_solution
