from random import randint

# [ 12, 14, 15, 20 ]
#    ^  ^
# ORDENAÇÃO: n*log(n)
# COMPLEXIDADE: (n)(n-1)(n*log(n))/2
# IDENTIFICAR: condição de parada
# PROBLEMA: loop de trocas
# Ordena e captura disponiveis por disponibilidade e configuração

# maquina -> origem == ind. ativ -> config


# equipe
#  - maquina activeCheckSimulateAnnealing ||
#  - maquina
#  - maquina
#  - maquina
#  - maquina
# equipe
#  - maquina
#  - maquina
#  - maquina
#  - maquina
#  - maquina

def posicao_aleatoria(vetor):
    inicio = 0
    final = len(vetor)
    return randint(inicio, final-1)


class Trocador:
    # TODO precisamos validar na disponíveis se respeita janela inicial
    # TODO precisamos validar na disponíveis se respeita janela final

    def __init__(self, equipes, configuracoes):
        """
            @param equipes: recebe uma lista do tipo Equipe
            @param configuracoes: recebe a matriz de configuração
        """
        self.configuracoes = configuracoes
        self.equipes = equipes
        self.equipes_ordenadas = sorted(
            equipes, key=lambda x: x.disponibilidade)

    # ------------------------------------------

    def start(self):
        self.ordena_equipes_por_disponibilidade()
        equipe_origem = self.equipes[0]
        maquina = self.escolhe_maquina_aleatoria(equipe_origem)
        disponiveis = self.equipes_disponiveis(maquina)

        # TODO reaproveitar a origem
        disponiveis.remove(equipe_origem)

        if len(disponiveis) == 0:
            maquina.marcar()

            if equipe_origem.existe_equipe_valida():
                self.start()

            equipe_origem.liberar_maquinas_para_troca()
        else:
            pos_equipe_destino = posicao_aleatoria(disponiveis)
            equipe_destino = disponiveis[pos_equipe_destino]
            self.troca(equipe_origem, equipe_destino, maquina)

    # ------------------------------------------

    def troca(self, origem, destino, maquina):
        origem.maquinas.remove(maquina)
        destino.maquinas.append(maquina)
        maquina.reatribuir_equipe(destino)
        index = origem.maquinas.index(maquina)
        tempo_origem = origem.historico[index]

        print(f'trocando a maquina: {maquina}')
        print(f'origem: {origem}')
        print(f'destino: {destino}')

    # ------------------------------------------

    # esperou[l] = max(inicial[l] - historico[l-1], 0)
    # historico[l] = historico[l-1] + janela[l] + esperou[l]

    def corrige(self, equipe, index_inicial):
        pass  # TODO

    # ------------------------------------------

    def ordena_equipes_por_disponibilidade(self):
        def criterio_por_disponibilidade(equipe): return equipe.disponibilidade
        # * o sorted ordena de modo crescente por disponibilidade
        return sorted(self.equipes, key=criterio_por_disponibilidade, reverse=True)

    # ------------------------------------------

    def equipes_disponiveis(self, maquina):

        disponiveis_por_disponibilidade = self.captura_equipes_com_disponibilidade(
            maquina)
        disponiveis_por_configuracao = self.captura_equipes_por_configuracao(
            maquina)

        def comum(element): return element in disponiveis_por_disponibilidade
        interseccao = list(filter(comum, disponiveis_por_configuracao))

        return interseccao

    # ------------------------------------------

    def captura_equipes_com_disponibilidade(self, maquina):
        disponiveis = []
        configuracao = self.configuracoes[maquina.atividade]

        for i in range(len(configuracao)):
            valor = configuracao[i]

            if valor == 1:
                disponiveis.append(self.equipes[i])

        return disponiveis

    # ------------------------------------------

    def captura_equipes_por_configuracao(self, maquina):
        disponiveis = []

        for equipe in self.equipes:
            if equipe.disponibilidade > maquina.tempo_processamento:
                disponiveis.append(equipe)

        return disponiveis

    # ------------------------------------------

    def escolhe_maquina_aleatoria(self, equipe):
        """
            @param equipe: a equipe que terá uma máquina aleatória escolhida
            @return: maquina: maquina escolhida aleatoriamente
        """
        posicao = posicao_aleatoria(equipe.maquinas)
        return equipe.maquinas[posicao]

    # ------------------------------------------
