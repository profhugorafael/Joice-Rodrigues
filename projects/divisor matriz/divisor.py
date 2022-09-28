# bibliotecas
from random import randint

# ----------------------------------------------------
# declarando para fins de teste

# instancias['Configuração']
configuracao = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]

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
    ativos = descobreAtivos(configuracao[linha])
    distribuiParaAtivos(processamento[linha], ativos, equipes, linha)   

# ----------------------------------------------------
# descobre equipes ativas para receber este elemento

def descobreAtivos(vetor_binario):
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
    print(f'espaço: {janela_na_equipe_para_maquina} || custo {janela}')

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

    print(f'janela equipe {nome_equipe} para maquina {numero_da_maquina}: {janela_na_equipe_para_maquina}')
    print(f'tempo de janela: {janela}')

    if janela_na_equipe_para_maquina >= janela:
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
    
    ativos_por_fim = filtraAtivosPorJanelaFinal(maquina, ativos, equipes)
    ativos_por_inicio_e_fim = filtraAtivosPorJanelaInicial(maquina, ativos_por_fim, equipes)

    # DEBUG
    print(f' {ativos} || {ativos_por_fim} ')
    print(f' {ativos_por_fim} || {ativos_por_inicio_e_fim} ')
    
    pos = randint(0, len(ativos_por_inicio_e_fim)-1 )
    nome_equipe = 'eq' + str(ativos_por_inicio_e_fim[pos] + 1)

    equipe = equipes[nome_equipe]

    equipe['janela final local'][maquina_index] -= maquina['janela']
    equipe['janela inicial'][maquina_index] = 0
    
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
# aplicacao

divideMatriz(configuracao, processamentos, equipes)

for key in equipes.keys():
  print(f'# {key}')
  print(f'janela final local final : {equipes[key]["janela final local"]} ')
  print(f'janela total : {equipes[key]["janela total"]} ')
  print(f'consumo da janela inicial : {equipes[key]["janela inicial"]} ')

  for maquina in equipes[key]['maquinas']:
    print(f'{maquina}')

# ----------------------------------------------------