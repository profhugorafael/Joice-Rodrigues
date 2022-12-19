
# tamanho configuração = Total de equipes que podem receber um processamento
tamanho_configuracao = []

# checklist processamento = checa se um processamento ja ocorreu
checklist_processamento = []

numero_equipes = len(configuracoes[0])
equipes = dict()

for configuracao in configuracoes:
  tamanho_configuracao.append( sum(configuracao) )
  checklist_processamento.append(False)

for numero in range(numero_equipes):
  nome_equipe = 'eq' + str(numero+1)
  equipes[nome_equipe] = dict()
  equipes[nome_equipe]['janela final local'] = [ ]
  equipes[nome_equipe]['janela total'] = [ ]
  equipes[nome_equipe]['janela inicial'] = [ ]
  equipes[nome_equipe]['disponibilidade'] = janela_disponibilidade[numero]
  equipes[nome_equipe]['disponibilidade total'] = janela_disponibilidade[numero]
  equipes[nome_equipe]['tempo'] = 0
  
  for i in range(len(janela_final)):
    valor = janela_final[i]
    valor_inicial = janela_inicial[i]
    equipes[nome_equipe]['janela final local'].append(valor)
    equipes[nome_equipe]['janela total'].append(valor)
    equipes[nome_equipe]['janela inicial'].append(valor_inicial)

  equipes[nome_equipe]['maquinas'] = [ ]

def filtraAtivos(vetor_binario):
  ativos = [ ]

  for i in range( len(vetor_binario) ):
    if vetor_binario[i] : ativos.append(i)
  
  return ativos


assert filtraAtivos([0, 1, 1]) == [1, 2]

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

def ordenaPorJanelaFinal_desc(maquina, ativos, equipes) :

  numero_da_maquina = maquina['maquina de origem']
  ativos_com_janela_final = dict()

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)
    janela_final = equipes[nome_equipe]['janela final local']
    ativos_com_janela_final[ativo] = janela_final[numero_da_maquina]

  ordenados = sorted(ativos_com_janela_final.items(), key = lambda x:x[1], reverse = True)
  ordenados = list(dict(ordenados).keys())

  # DEBUG
  # print(f'dicionario temporario = {ativos_com_janela_final}')
  # print(f'ordenados = {ordenados}')

  return ordenados

def ordenaPorJanelaInicial_asc(maquina, ativos, equipes) : 
  
  numero_da_maquina = maquina['maquina de origem']
  ativos_com_janela_inicial = dict()

  for i in range( len(ativos) ):
    ativo = ativos[i]
    nome_equipe = 'eq' + str(ativo + 1)
    janela_inicial = equipes[nome_equipe]['janela inicial']
    ativos_com_janela_inicial[ativo] = janela_inicial[numero_da_maquina]

  ordenados = sorted(ativos_com_janela_inicial.items(), key = lambda x:x[1])
  ordenados = list(dict(ordenados).keys())

  # DEBUG
  # print(f'dicionario temporario = {ativos_com_janela_inicial}')
  # print(f'ordenados = {ordenados}')

  return ordenados


def processaJanelaInicial(maquina, equipe):

  numero_da_maquina = maquina['maquina de origem']
  janela = maquina['janela'] 
    
  horario_autorizado = equipe['janela inicial'][numero_da_maquina]

  # precisa esperar ?
  tempo = max(equipe['tempo'], horario_autorizado) + janela
  
  equipe['tempo'] = tempo  


def distribuiParaAtivos(processamento, ativos, equipes, indice_atividade, contador) :

  for maquina_index in range( len(processamento) ):

    maquina = {
      'janela': processamento[maquina_index],
      'indice da atividade': indice_atividade,
      'maquina de origem': maquina_index
    }

    # print(f'maquina = {maquina}')
    
    # ativos 1 = filtrados pela janela final
    ativos1 = filtraAtivosPorJanelaFinal(maquina, ativos, equipes)
    print(f'ativos1 = {ativos1}')

    # ativos 2 = filtrados pela disponibilidade da equipe
    ativos2 = filtraAtivosPorDisponibilidade(maquina, ativos1, equipes)
    print(f'ativos2 = {ativos2}')

    # ordenados 1 = filtrando por janela final de modo decrescente
    ordenados1 = ordenaPorJanelaFinal_desc(maquina, ativos2, equipes)

    # tenho certeza que o tamanho será necessariamente maior que zero
    assert len(ordenados1) > 0, printEquipes(contador)
    print(f'ordenados1 = {ordenados1}')

    # ordenados 2 = filtrando por janela inicial de modo crescente
    ordenados2 = ordenaPorJanelaInicial_asc(maquina, ordenados1, equipes)

    # tenho certeza que o tamanho será necessariamente maior que zero
    assert len(ordenados2) > 0, printEquipes(contador)
    print(f'ordenados2 = {ordenados2}')
    
    print('-----------------------------------------')

    # acesso a posição
    ## monto o nome da equipe em funcao dos filtrados
    numero_equipe_escolhida = ordenados2[0]
    nome_equipe = 'eq' + str(numero_equipe_escolhida + 1)
   
    # acesso a equipe que receberá a maquina
    equipe = equipes[nome_equipe]
    
    #processando janela inicial
    # ainda não valida se o tempo total é menor que a janela final
    ativos2 = processaJanelaInicial(maquina, equipe)

    equipe['janela final local'][maquina_index] -= maquina['janela']
    equipe['disponibilidade'] -= maquina['janela']
    
    # DEBUG
    # print(f'A equipe {nome_equipe} recebeu na maquina {maquina_index} menos {maquina["janela"]}')

    equipe['maquinas'].append(maquina)


def divideMatriz(configuracoes, processamento, equipes):

  contador = 0
  max_equipes = len(configuracoes[0]) + 1

  for quantidade_equipes_autorizadas in range(max_equipes):
    
    for linha in range( len(configuracoes) ):
      tamanho_autorizado = tamanho_configuracao[linha] == quantidade_equipes_autorizadas

      if tamanho_autorizado and not checklist_processamento[linha]:
        checklist_processamento[linha] = True
        ativos = filtraAtivos(configuracoes[linha])
        distribuiParaAtivos(processamento[linha], ativos, equipes, linha, contador)
        contador += 1


