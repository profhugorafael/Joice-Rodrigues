CTE.equipes
prefix = './test/'
filenames = ['teste1.txt', 'teste2.txt' 'teste3.txt']
tolerancia = 5

for filename in filenames:
  file = prefix + filename
  var = run(file)


  var <= esperado + tolerancia or var >= esperado - tolerancia ? PASSED : FAILED