from model.Maquina import Maquina

class Filtro:

    # ------------------------------------------
    def __init__(self, maquina: Maquina, equipes_disponiveis):
        self.equipes_disponiveis = equipes_disponiveis
        self.maquina = maquina

    # ------------------------------------------

    def filtraAtivosPorJanelaFinal(self):
        disponiveis_pos_filtro = []

        for equipe in self.equipes_disponiveis:

            tempo_disponivel = equipe.janela_final[self.maquina.index]

            if tempo_disponivel >= self.maquina.tempo_processamento:
                disponiveis_pos_filtro.append(equipe)

        self.equipes_disponiveis = disponiveis_pos_filtro.copy()

    # ------------------------------------------

    def filtraAtivosPorDisponibilidade(self):
        disponiveis_pos_filtro = []

        for equipe in self.equipes_disponiveis:
            if equipe.disponibilidade >= self.maquina.tempo_processamento:
                disponiveis_pos_filtro.append(equipe)

        self.equipes_disponiveis = disponiveis_pos_filtro.copy()

    # ------------------------------------------

    def ordenaPorJanelaFinal_desc(self):
        ordenacao = sorted(
            self.equipes_disponiveis,
            key=lambda e: e.janela_final,
            reverse=True)

        self.equipes_disponiveis = ordenacao.copy()

    # ------------------------------------------

    def ordenaPorJanelaInicial_asc(self):

        ordenacao = sorted(
            self.equipes_disponiveis,
            key=lambda equipe: equipe.janela_inicial
        )

        self.equipes_disponiveis = ordenacao.copy()
