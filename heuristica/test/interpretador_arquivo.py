
# -----------------------------

QUEBRA_DE_LINHA = '\n'
instancias = dict()
keys = ['Processamento', 'Janela Inicial', 'Janela Final', 'Maquinas', 'Atividades', 'Equipes','Configuração', 'Horas Equipes']

# -----------------------------
# transformando para vetor

def linhaParaVetor(linha):
  linha = linha.split()
  
  for index in range( len(linha) ):
    linha[index] = int( linha[index] )

  return linha

# -----------------------------
# corrigindo matrizes de apenas uma linha

def corrigeMatrizEmVetor(matriz) :
  if ( len(matriz) == 1 ) :
    aux = [ ]
    for elemento in matriz[0]:
      aux.append(elemento)
    return aux
  
  return matriz

# -----------------------------
# atualizando sequencia de chaves

def getNextKey():
  key = keys[0]
  keys.remove(key)
  return key

# -----------------------------

def leArquivoMatriz( nomeDoArquivo ) :

  matriz = [ ]

  with open(nomeDoArquivo) as arquivo :
    for linha in arquivo.readlines():
      if linha == QUEBRA_DE_LINHA :
        nextKey = getNextKey()
        matriz = corrigeMatrizEmVetor(matriz)
        instancias[nextKey] = matriz
        matriz = []
      else :
        vetor = linhaParaVetor(linha)
        matriz.append(vetor)

# -----------------------------

leArquivoMatriz('instancia1.txt')

print('---------------------------')

for key in instancias.keys() :
  print(key)
  print(instancias[key])
  print('---------------------------')

def processaInstancias(nomeDoArquivo: str):

  leArquivoMatriz(nomeDoArquivo + '.txt')

  configuracoes = instancias['Configuração']

  # Janela Final = capacidade de processamento de cada maquina
  janela_final = instancias['Janela Final']

  # Janela Inicial = tempo em que cada maquina deveria começar
  janela_inicial = instancias['Janela Inicial']

  # processamento = atividade x maquina
  processamentos = instancias['Processamento']

  janela_disponibilidade = instancias['Horas Equipes']

# ----------------------------------------------------
