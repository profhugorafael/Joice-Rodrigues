def tempo_da_equipe_maior_tempo_gasto(equipes):

  maior_tempo = -1

  for i in range(len(equipes)) :
    nome_equipe = 'eq' + str(i + 1)
    equipe = equipes[nome_equipe]

    tempo_gasto = equipe['tempo']

    if tempo_gasto > maior_tempo:
      maior_tempo = tempo_gasto

  return maior_tempo



def calcula_processamento(maquinas):
  soma = 0
  for maquina in maquinas:
    soma += maquina['janela']

  return soma


def printEquipes(contador):
  for key in equipes.keys():
    print(f'# {key}')
    print(f'janela final local final : {equipes[key]["janela final local"]} ')
    print(f'processamento = {calcula_processamento(equipes[key]["maquinas"])}')

    for maquina in equipes[key]['maquinas']:
      print(f'{maquina}')

    print(f'contagem de maquinas processadas = {contador}')


    