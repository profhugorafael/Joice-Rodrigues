# bibliotecas
from random import randint

# ----------------------------------------------------
# declarando para fins de teste

# instancias['Configuração']
configuracao = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]

# Janela Final = capacidade de processamento de cada maquina
janela_final = [20, 10, 21, 15]

# instancias['Processamento']
# processamento = atividade x maquina
processamentos = [ [4, 5, 10, 1],
                  [4, 5, 12, 1],
                  [4, 7, 13, 1] ]

# ----------------------------------------------------
# criacao das equipes (indexadas em 1)

numero_equipes = len(configuracao[0])
equipes = dict()

for numero in range(numero_equipes):
  nome_equipe = 'eq' + str(numero+1)
  equipes[nome_equipe] = dict()
  equipes[nome_equipe]['janela total'] = [ ]
  
  for valor in janela_final:
    equipes[nome_equipe]['janela total'].append(valor)

  equipes[nome_equipe]['maquinas'] = [ ]
  
# ----------------------------------------------------
# subdivide

def divideMatriz(configuracao, processamento, equipes):

  for linha in range( len(configuracao) ) :
    ativos = descobreAtivos(configuracao[linha])
    distribuiParaAtivos(processamento[linha], ativos, equipes)   

# ----------------------------------------------------
# descobre equipes ativas para receber este elemento

def descobreAtivos(vetor_binario):
  ativos = [ ]

  for i in range( len(vetor_binario) ):
    if vetor_binario[i] : ativos.append(i)
  
  return ativos

# ----------------------------------------------------
# filtra ativos por EQ

def filtraAtivosPorJanela(maquina, ativos, equipes):

  numero_da_maquina = maquina['maquina de origem']
  janela = maquina['janela']
  ativos_temporarios = [ ]

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)
    print(f'{nome_equipe}')
    equipe = equipes[nome_equipe]
    janela_na_equipe_para_maquina = equipe['janela total'][numero_da_maquina]

    print(f'espaço: {janela_na_equipe_para_maquina} || custo {janela}')

    if janela_na_equipe_para_maquina >= janela:
      ativos_temporarios.append(ativo)

  return ativos_temporarios

# ----------------------------------------------------
# distribui para as equipes ativas aleatoriamente

def distribuiParaAtivos(origem, ativos, equipes) :
  
  for maquina_index in range( len(origem) ):
    maquina = {
      'janela': origem[maquina_index],
      'maquina de origem': maquina_index
    }
    
    ativos_temporarios = filtraAtivosPorJanela(maquina, ativos, equipes)
    print(f' {ativos_temporarios} || {ativos} ')
    pos = randint(0, len(ativos_temporarios)-1 )
    nome_equipe = 'eq' + str(ativos_temporarios[pos] + 1)

    equipe = equipes[nome_equipe]

    equipe['janela total'][maquina_index] -= maquina['janela']
    print(f'A equipe {nome_equipe} recebeu na maquina {maquina_index} menos {maquina["janela"]}')

    equipe['maquinas'].append(maquina)

    print('-------------------')
    printEquipes()
    print('-------------------')
    # print(janela_final)

def printEquipes():
  for key in equipes.keys():
    print(f'# {key}')
    print(f'janela total final : {equipes[key]["janela total"]} ')

    for maquina in equipes[key]['maquinas']:
      print(f'{maquina}')

# ----------------------------------------------------
# aplicacao

divideMatriz(configuracao, processamentos, equipes)

for key in equipes.keys():
  print(f'# {key}')
  print(f'janela total final : {equipes[key]["janela total"]} ')

  for maquina in equipes[key]['maquinas']:
    print(f'{maquina}')

# ----------------------------------------------------