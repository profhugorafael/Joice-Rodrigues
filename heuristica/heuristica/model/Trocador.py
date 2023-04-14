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
    aleatorio = randint(inicio, final-1)
    print(f'\n( size: **{final}**, random: **{aleatorio})**\n ')
    return aleatorio


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
        posicao_saida = posicao_aleatoria(equipe_origem.maquinas)
        maquina = equipe_origem.maquinas[posicao_saida]

        disponiveis = self.equipes_disponiveis(maquina)

        posicao_equipe_destino = posicao_aleatoria(disponiveis)
        equipe_destino = disponiveis[posicao_equipe_destino]
        posicao_entrada = posicao_aleatoria(equipe_destino.maquinas)

        self.troca(equipe_origem, equipe_destino,
                   posicao_entrada, posicao_saida)

    # ------------------------------------------

    def troca(self, origem, destino, entrada, saida):

        if origem != destino and len(origem.maquinas) != len(destino.maquinas):
            print('## Erro aqui! :x:')

        print('## trocando a maquina...\n\n')
        print(
            f'- tamanhos: (**origem:** {len(origem.maquinas)} , **destino:** {len(destino.maquinas)})')

        print(f'- origem: {origem.id} + linha_saida: {saida}\n')
        maquina = origem.maquinas.pop(saida)
        historico_anterior = origem.historico.pop(saida)
        self.corrige(origem, saida)

        print(f'- destino: {destino.id} + linha_entrada: {entrada}\n')
        destino.maquinas.insert(entrada, maquina)
        destino.historico.insert(entrada, historico_anterior)
        self.corrige(destino, entrada)

        print(f'- maquina {maquina}')
        print('- trocado!\n\n')

    # ------------------------------------------

    # historico_anterior = historico[l - 1]
    # esperou[l] = max(inicial[l] - historico_acumulado, 0)
    # historico[l] = historico_anterior + janela[l] + esperou[l]

    def corrige(self, equipe, linha):
        if linha < 0 or linha >= len(equipe.maquinas):
            # print(f'\t\tparando... (linha: {linha})\n')
            return

        # print(f'\t\tid = {equipe.id}, corrigindo linha: {linha}\n')
        maquina = equipe.maquinas[linha]

        inicial_linha = equipe.janela_inicial[maquina.index]
        janela = maquina.tempo_processamento

        historico_anterior = equipe.historico[linha - 1] if linha != 0 else 0
        delta_espera = inicial_linha - historico_anterior
        esperou_atual = max(delta_espera, 0)

        equipe.historico[linha] = historico_anterior + janela + esperou_atual

        self.corrige(equipe, linha+1)

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

    def captura_equipes_por_configuracao(self, maquina):
        disponiveis = []
        configuracao = self.configuracoes[maquina.atividade]

        for i in range(len(configuracao)):
            valor = configuracao[i]

            if valor == 1:
                disponiveis.append(self.equipes[i])

        return disponiveis

    # ------------------------------------------

    def captura_equipes_com_disponibilidade(self, maquina):
        disponiveis = []

        for equipe in self.equipes:
            if equipe.tempo_livre >= maquina.tempo_processamento:
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
