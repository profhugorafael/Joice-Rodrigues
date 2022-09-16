# bibliotecas
from random import randint

# ----------------------------------------------------
# declarando para fins de teste

# instancias['Configuração']
configuracao = [[1, 0], [1, 1], [0, 1]]

# Janela Final = capacidade de processamento de cada maquina
janela_final = [20, 10, 21, 15]

# instancias['Processamento']
# processamento = atividade x maquina
processamento = [ [7, 4, 6, 9],
                  [7, 9, 5, 1],
                  [8, 12, 9, 2] ]

# ----------------------------------------------------
# criacao das equipes (indexadas em 1)

numero_equipes = len(configuracao[0])
equipes = dict()

for numero in range(numero_equipes):
  nome_equipe = 'eq' + str(numero+1)
  equipes[nome_equipe] = dict()
  equipes[nome_equipe]['janela_total'] = janela_final
  equipes[nome_equipe]['maquinas'] = [ ]
  
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
  
  for maquina in range( len(origem) ):
    
    pos = randint(0, len(ativos) - 1)

    while(ativos[pos][])

    nome_equipe = 'eq' + str(ativos[pos] + 1)

    entrada = {
      'tempo': origem[maquina],
      'maquina de origem': maquina
    }

    janela_final[maquina] -= entrada['tempo']
    equipes[nome_equipe].append(entrada)
    print(janela_final)

# ----------------------------------------------------
# aplicacao

divideMatriz(configuracao, processamento, equipes)

for key in equipes.keys() :
    print(f'# {key}')
    
    for elemento in equipes[key]:
      print(f'{elemento}')

print(janela_final)
# ----------------------------------------------------