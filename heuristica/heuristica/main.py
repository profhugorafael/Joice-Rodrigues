import model.Equipe as Equipe

from model.Processador import Processador
from model.Trocador import Trocador
from model.FileManipulator import FileManipulator
from cmath import exp as complex_exp
from random import uniform as uniform_random

# ------------------------------------
# UTILITÁRIO


def exp(number): return complex_exp(number).real

# ------------------------------------


def initial_solution(filename):
    dados = FileManipulator(f'{filename}.txt')
    processador = Processador(dados)
    processador.inicializar_equipes()
    while processador.processar_proximo():
        continue

    print(processador)
    for equipe in processador.equipes:
        print(f"## Equipe {equipe.id}")
        print(equipe.tabela_maquinas())

    return processador.equipes, dados.configuracoes

# ------------------------------------


def generate_neighbor(equipes, configuracoes):
    print('\n----\n')
    copia_equipes = equipes.copy()
    neighbor_generator = Trocador(copia_equipes, configuracoes)
    neighbor_generator.start()
    return copia_equipes

# ------------------------------------


def energy(equipes):
    maior_tempo = -1

    for equipe in equipes:
        if equipe.tempo_de_processamento > maior_tempo:
            maior_tempo = equipe.tempo_de_processamento

    return maior_tempo

# ------------------------------------


def simulated_annealing(istance_id, temperature, cooling_rate, freeze_temperature, max_iterations):
    # machines: lista de máquinas
    # temperature: temperatura inicial
    # teams: lista de equipe
    # cooling_rate: taxa de resfriamento (0, 1) - decimal value
    # max_iterations: número máximo de iterações

    # Inicializa a solução atual com uma distribuição aleatória de máquinas em equipes
    base_solution, teams_configuration = initial_solution(
        f'instancia{istance_id}')

    current_solution = base_solution.copy()
    best_solution = current_solution

    # Loop principal
    while temperature > freeze_temperature:
        for _ in range(max_iterations):
            # Gera uma nova solução a partir da solução atual
            new_solution = generate_neighbor(
                current_solution, teams_configuration)

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

    return base_solution, best_solution

# ------------------------------------


print("# Heuristica\n")

sol_inicial, sol_final = simulated_annealing(3, 100, 0.6, 20, 10)
tempo_max_inicial = -1
tempo_max_final = -1

for equipe in sol_inicial:
    if equipe.tempo_de_processamento > tempo_max_inicial:
        tempo_max_inicial = equipe.tempo_de_processamento

print(f"**TEMPO MAXIMO SOL INICIAL =** {tempo_max_inicial}")

for equipe in sol_final:
    if equipe.tempo_de_processamento > tempo_max_final:
        tempo_max_final = equipe.tempo_de_processamento

for equipe in sol_final:
    print(f"## Equipe {equipe.id}")
    print(equipe.tabela_maquinas())

print(f"TEMPO MAX INICIAL: {tempo_max_inicial}\n")
print(f"TEMPO MAX FINAL: {tempo_max_final}")
