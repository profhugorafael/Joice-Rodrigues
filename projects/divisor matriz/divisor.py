# bibliotecas
from random import randint

# ----------------------------------------------------
# declarando para fins de teste

# instancias['Configuração']
configuracao = [[1, 0], [1, 1], [0, 1]] 

# instancias['Processamento']
processamento = [[3, 3, 4, 1], [2, 3, 1, 1], [1, 1, 1, 2]]

# ----------------------------------------------------
# criacao das equipes (indexadas em 1)

numero_equipes = len(configuracao[0])
equipes = dict()

for numero in range(numero_equipes):
  nome_equipe = 'eq' + str(numero+1)
  equipes[nome_equipe] = [ ]

# ----------------------------------------------------
# subdivide

def divideMatriz(configuracao, processamento, equipes):


  for linha in range( len(configuracao) ) :
    ativos = descobreAtivos(configuracao[linha])
    distribuiParaAtivos(processamento[linha], ativos, equipes)   

# ----------------------------------------------------
# descobre equipes ativas para receber este elemento

def descobreAtivos(vetorBinario):
  ativos = [ ]

  for i in range( len(vetorBinario) ):
    if vetorBinario[i] : ativos.append(i)
  
  return ativos

# ----------------------------------------------------
# distribui para as equipes ativas aleatoriamente

def distribuiParaAtivos(origem, ativos, equipes) :
  
  for valor in origem:
    pos = randint(0, len(ativos) - 1)
    nome_equipe = 'eq' + str(ativos[pos] + 1)
    # print(f'{valor} vai para {nome_equipe}')
    equipes[nome_equipe].append(valor)

# ----------------------------------------------------
# aplicacao

divideMatriz(configuracao, processamento, equipes)

for key in equipes.keys() :
    print(f'{key} : {equipes[key]}')
# ----------------------------------------------------