class Maquina:

    def __init__(self, tempo_processamento, indice_atividade, index_maquina):
        self.index = index_maquina
        self.tempo_processamento = tempo_processamento
        self.tempo_de_espera = 0
        self.janela_inicial = 0
        self.atividade = indice_atividade
        self.invalida = False

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

    def __str__(self):
        return f'| {self.tempo_processamento} | {self.atividade} | {self.index} | {self.janela_inicial} | {self.tempo_de_espera} |'
