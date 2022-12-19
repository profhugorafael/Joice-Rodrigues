import Leitura_de_instancias as li
import Solucao_Inicial_Gulosa as SIL
import Calcula_Makespan as CA


# tamanho configuração = Total de equipes que podem receber um processamento
tamanho_configuracao = []

# checklist processamento = checa se um processamento ja ocorreu
checklist_processamento = []

sol = li.leArquivoMatriz(x)
print(sol)
'''
divideMatriz(configuracoes, processamentos, equipes)

print('-------------------------------------------------')

for key in equipes.keys():
  print(f'# {key}')
  print(f'disponibilidade total : {equipes[key]["disponibilidade total"]} ')
  print(f'disponibilidade resultante : {equipes[key]["disponibilidade"]} ')
  print(f'tempo gasto da equipe total : {equipes[key]["tempo"]}')
  print(f'janela final local : {equipes[key]["janela final local"]} ')
  print(f'janela total : {equipes[key]["janela total"]} ')
  print(f'janela inicial : {equipes[key]["janela inicial"]} ')
  print('-------------------------------------------------')

  for maquina in equipes[key]['maquinas']:
    print(f'{maquina}')

tempo_maior = tempo_da_equipe_maior_tempo_gasto(equipes)
print(f'MAIOR TEMPO GASTO EM UMA EQUIPE: {tempo_maior}')
'''