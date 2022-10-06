# bibliotecas
from random import randint

# ----------------------------------------------------
# declarando para fins de teste

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

# ----------------------------------------------------
# criacao das equipes (indexadas em 1)

numero_equipes = len(configuracao[0])
equipes = dict()

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
  
# ----------------------------------------------------
# subdivide

def divideMatriz(configuracao, processamento, equipes):

  for linha in range( len(configuracao) ) :
    ativos = filtraAtivos(configuracao[linha])
    distribuiParaAtivos(processamento[linha], ativos, equipes, linha)   

# ----------------------------------------------------
# descobre equipes ativas para receber este elemento

def filtraAtivos(vetor_binario):
  ativos = [ ]

  for i in range( len(vetor_binario) ):
    if vetor_binario[i] : ativos.append(i)
  
  return ativos

# ----------------------------------------------------
# filtra ativos por EQ

def filtraAtivosPorJanelaFinal(maquina, ativos, equipes):

  numero_da_maquina = maquina['maquina de origem']
  janela = maquina['janela']
  ativos_temporarios = [ ]

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)

    # DEBUG
    # print(f'{nome_equipe}')
    
    equipe = equipes[nome_equipe]
    janela_na_equipe_para_maquina = equipe['janela final local'][numero_da_maquina]

    # DEBUG
    # print(f'espaço: {janela_na_equipe_para_maquina} || custo {janela}')

    if janela_na_equipe_para_maquina >= janela:
      ativos_temporarios.append(ativo)

  return ativos_temporarios

# ----------------------------------------------------

def filtraAtivosPorJanelaInicial(maquina, ativos, equipes):

  numero_da_maquina = maquina['maquina de origem']
  janela = maquina['janela'] 
  ativos_temporarios = [ ]

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)

    equipe = equipes[nome_equipe]
    
    janela_inicial = equipe['janela inicial'][numero_da_maquina]
    janela += janela_inicial
    janela_na_equipe_para_maquina = equipe['janela final local'][numero_da_maquina]
    
    # DEBUG
    # print(f'janela equipe {nome_equipe} para maquina {numero_da_maquina}: {janela_na_equipe_para_maquina}')
    # print(f'tempo de janela: {janela}')

    if janela_na_equipe_para_maquina >= janela:
      ativos_temporarios.append(ativo)

  return ativos_temporarios

# ----------------------------------------------------

def filtraAtivosPorDisponibilidade(maquina, ativos, equipes):
  
  numero_da_maquina = maquina['maquina de origem']
  janela = maquina['janela'] 
  ativos_temporarios = [ ]

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)
    equipe = equipes[nome_equipe]
    disponibilidade = equipe['disponibilidade']
    
    # DEBUG
    # print(f'janela equipe {nome_equipe} para maquina {numero_da_maquina}: {janela_na_equipe_para_maquina}')
    # print(f'tempo de janela: {janela}')

    if disponibilidade >= janela:
      ativos_temporarios.append(ativo)

  return ativos_temporarios

# ----------------------------------------------------
# distribui para as equipes ativas aleatoriamente

def distribuiParaAtivos(origem, ativos, equipes, indice_atividade) :
  
  for maquina_index in range( len(origem) ):

    maquina = {
      'janela': origem[maquina_index],
      'indice da atividade': indice_atividade,
      'maquina de origem': maquina_index
    }
    
    # ativos 1 = filtrados pela janela final
    ativos1 = filtraAtivosPorJanelaFinal(maquina, ativos, equipes)

    # ativos 2 = filtados pela janela inicial
    ativos2 = filtraAtivosPorJanelaInicial(maquina, ativos1, equipes)

    # ativos 3 = filtrados pela disponibilidade da equipe
    ativos3 = filtraAtivosPorDisponibilidade(maquina, ativos2, equipes)

    # DEBUG
    # print(f'ATIVOS = {ativos1} ')
    # print(f'POR FINAL = {ativos2} ')
    # print(f'POR INICIAL = {ativos3} ')
    # print(f'POR DISPONIBILIDADE = {ativos3} ')
    
    # resgato a posicao em cima do ultimo filtro
    pos = randint(0, len(ativos3)-1 )

    ## monto o nome da equipe em funcao dos filtrados
    nome_equipe = 'eq' + str(ativos3[pos] + 1)

    equipe = equipes[nome_equipe]

    equipe['janela final local'][maquina_index] -= maquina['janela']
    equipe['janela inicial'][maquina_index] = 0
    equipe['disponibilidade'] -= maquina['janela']
    
    # DEBUG
    # print(f'A equipe {nome_equipe} recebeu na maquina {maquina_index} menos {maquina["janela"]}')

    equipe['maquinas'].append(maquina)
  
    # DEBUG
    # print('-------------------')
    # printEquipes()
    # print('-------------------')
    # print(janela_final)

# ----------------------------------------------------
# imprime resultados das equipes distribuidas

def printEquipes():
  for key in equipes.keys():
    print(f'# {key}')
    print(f'janela final local final : {equipes[key]["janela final local"]} ')

    for maquina in equipes[key]['maquinas']:
      print(f'{maquina}')

# ----------------------------------------------------

def tempo_da_equipe_maior_tempo_gasto(equipes):

  maior_tempo = -1

  for i in range(len(equipes)) :
    nome_equipe = 'eq' + str(i + 1)
    equipe = equipes[nome_equipe]

    tempo_gasto = equipe["disponibilidade total"] - equipe["disponibilidade"]

    if tempo_gasto > maior_tempo:
      maior_tempo = tempo_gasto

  return maior_tempo

# ----------------------------------------------------
# aplicacao

divideMatriz(configuracao, processamentos, equipes)

for key in equipes.keys():
  print(f'# {key}')
  print(f'disponibilidade total : {equipes[key]["disponibilidade total"]} ')
  print(f'disponibilidade resultante : {equipes[key]["disponibilidade"]} ')
  print(f'tempo gasto da equipe total : {equipes[key]["disponibilidade total"] - equipes[key]["disponibilidade"]} ')
  print(f'janela final local final : {equipes[key]["janela final local"]} ')
  print(f'janela total : {equipes[key]["janela total"]} ')
  print(f'consumo da janela inicial : {equipes[key]["janela inicial"]} ')

  for maquina in equipes[key]['maquinas']:
    print(f'{maquina}')

tempo_maior = tempo_da_equipe_maior_tempo_gasto(equipes)
print(f'MAIOR TEMPO GASTO EM UMA EQUIPE: {tempo_maior}')

# ----------------------------------------------------