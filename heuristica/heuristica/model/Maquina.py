class Maquina:

    def __init__(self, tempo_processamento, indice_atividade, index_maquina):
        self.tempo_processamento = tempo_processamento
        self.atividade = indice_atividade
        self.index = index_maquina
        self.invalida = False

    def __str__(self):
        return f'tempo de processamento {self.tempo_processamento} | indice atividade : {self.atividade} | maquina de origem : {self.index}'

    def atribuir_equipe(self, equipe):
        self.equipe = equipe
        self.atribuida = True

    def reatribuir_equipe(self, equipe):
        if not self.atribuida:
            return
        self.equipe = equipe

    def marcar(self):
        self.invalida = True

    def desmarcar(self):
        self.invalida = False
