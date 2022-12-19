# TEMPO
tempo = 0

# instancias['Configuração']
configuracao = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]

# janela Disponibilidade = Disponibilidade total de tempo de uma equipe
janela_disponibilidade = [40, 50, 45]

# Janela Final = capacidade de processamento de cada maquina
janela_final = [20, 10, 21, 15]

# Janela Inicial = tempo em que cada maquina deveria começar
janela_inicial = [3, 3, 4, 7]

# instancias['Processamento']
# processamento = atividade x maquina
processamentos = [ [4, 5, 4, 1],
                  [4, 5, 6, 1],
                  [4, 7, 3, 1] ]

# criacao das equipes (indexadas em 1)
numero_equipes = len(configuracao[0])
equipes = dict()

def inicializar(): 
  for numero in range(numero_equipes):
    nome_equipe = 'eq' + str(numero+1)
    equipes[nome_equipe] = dict()
    equipes[nome_equipe]['janela final local'] = [ ]
    equipes[nome_equipe]['janela total'] = [ ]
    equipes[nome_equipe]['janela inicial'] = [ ]
    equipes[nome_equipe]['disponibilidade'] = janela_disponibilidade[numero]
    equipes[nome_equipe]['disponibilidade total'] = janela_disponibilidade[numero]
    
    for i in range(len(janela_final)):
      valor = janela_final[i]
      valor_inicial = janela_inicial[i]
      equipes[nome_equipe]['janela final local'].append(valor)
      equipes[nome_equipe]['janela total'].append(valor)
      equipes[nome_equipe]['janela inicial'].append(valor_inicial)

    equipes[nome_equipe]['maquinas'] = [ ]