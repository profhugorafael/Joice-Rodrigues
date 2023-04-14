from model.Maquina import Maquina


class Filtro:

    # ------------------------------------------
    def __init__(self, maquina: Maquina, equipes_disponiveis):
        self.equipes_disponiveis = equipes_disponiveis
        self.maquina = maquina

    # ------------------------------------------

    def filtra__por_janela_final(self):
        disponiveis_pos_filtro = []

        for equipe in self.equipes_disponiveis:

            tempo_disponivel = equipe.janela_final[self.maquina.index]

            if tempo_disponivel >= self.maquina.tempo_processamento:
                disponiveis_pos_filtro.append(equipe)

        self.equipes_disponiveis = disponiveis_pos_filtro.copy()

    # ------------------------------------------

    def filtra_por_disponibilidade(self):
        disponiveis_pos_filtro = []

        for equipe in self.equipes_disponiveis:
            if equipe.disponibilidade >= self.maquina.tempo_processamento:
                disponiveis_pos_filtro.append(equipe)

        self.equipes_disponiveis = disponiveis_pos_filtro.copy()

    # ------------------------------------------

    def ordena(self, por, ordem):

        ordem = True if (ordem == 'decrescente') else False

        ordenacao = sorted(
            self.equipes_disponiveis,
            key=lambda equipe: getattr(equipe, por),
            reverse=ordem
        )

        self.equipes_disponiveis = ordenacao.copy()
