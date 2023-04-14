from model.Equipe import Equipe
from model.FileManipulator import FileManipulator
from model.Filtro import Filtro
from model.Maquina import Maquina


def eh_equipe(elemento):
    return True if isinstance(elemento, Equipe) else False


def highligth(msg):
    print()
    print(f'> {msg}')
    print()


class Processador:

    def __init__(self, dados: FileManipulator):
        self.dados = dados
        self.equipes = []
        self.index = 0
        self.__soma_atual__ = 1
        self.__checklist_configuracoes__ = []
        self.limit = len(self.dados.configuracoes[0])

        for _ in range(len(self.dados.configuracoes)):
            self.__checklist_configuracoes__.append(False)

    # ------------------------------------------

    def inicializar_equipes(self):
        quantidade = len(self.dados.configuracoes[0])

        for i in range(quantidade):
            equipe = Equipe(
                id=i,
                disponibilidade=self.dados.disponibilidades[i],
                janela_final=self.dados.janelas_finais,
                janela_inicial=self.dados.janelas_iniciais
            )

            if eh_equipe(equipe):
                self.equipes.append(equipe)

    # ------------------------------------------

    def processar_proximo(self) -> bool:

        if self.__alcancou_limite__():
            self.exibe_checklist_configuracao()
            print('\n\n--------\n')
            return False

        self.index = self.__proximo_index__()

        configuracao = self.dados.configuracoes[self.index]
        equipes_disponiveis = self.__captura_equipes_disponiveis__(
            configuracao)
        self.__distribui_para_equipes_disponiveis__(equipes_disponiveis)

        self.index += 1
        return True

    # ------------------------------------------

    def encontra_equipe_com_maior_tempo(self) -> Equipe:
        equipe_maior_tempo = self.equipes[0]

        for equipe in self.equipes:
            equipe_maior_tempo = max(equipe, equipe_maior_tempo)

        return equipe_maior_tempo

    # ------------------------------------------

    def __distribui_para_equipes_disponiveis__(self, equipes_disponiveis):

        processamento = self.dados.processamentos[self.index]

        for index_maquina in range(len(processamento)):

            maquina = Maquina(
                tempo_processamento=processamento[index_maquina],
                index_maquina=index_maquina,
                indice_atividade=self.index
            )

            filtro = Filtro(maquina, equipes_disponiveis)
            filtro.filtra__por_janela_final()
            filtro.filtra_por_disponibilidade()
            filtro.ordena(
                por='janela_final',
                ordem='decrescente'
            )
            filtro.ordena(
                por='janela_inicial',
                ordem='crescente'
            )

            assert len(filtro.equipes_disponiveis) > 0, self

            indice_para_receber = filtro.equipes_disponiveis[0].id
            equipe_destino = self.equipes[indice_para_receber]
            equipe_destino.adiciona_maquina(maquina)

    # ------------------------------------------

    def __captura_equipes_disponiveis__(self, configuracao):
        disponiveis = []

        for i in range(len(configuracao)):
            if configuracao[i]:
                equipe = self.equipes[i]
                if eh_equipe(equipe):
                    disponiveis.append(equipe)

        return disponiveis

    # ------------------------------------------

    def __proximo_index__(self):

        self.exibe_checklist_configuracao()

        for i in range(len(self.dados.configuracoes)):
            configuracao = self.dados.configuracoes[i]
            soma = sum(configuracao)  # 1 a n
            processado = self.__checklist_configuracoes__[i]

            if soma == self.__soma_atual__ and not processado:
                self.__checklist_configuracoes__[i] = True
                return i

        self.__soma_atual__ += 1
        if not self.__alcancou_limite__():
            return self.__proximo_index__()

    # ------------------------------------------

    def exibe_checklist_configuracao(self):
        print(f'soma: {self.__soma_atual__} | ', end='')
        print('config = [', end=' ')
        for x in self.__checklist_configuracoes__:
            print(' ' if x else "X", end=', ')
        print(']\n')

    # ------------------------------------------

    def __alcancou_limite__(self) -> bool:

        if self.__soma_atual__ > self.limit:
            return True

        for linha in self.__checklist_configuracoes__:
            if not linha:
                return False

        return True

    # ------------------------------------------

    def __str__(self):
        aux = "Equipe | Total | Utilizado | Livre |\n"
        aux += "| :-: | :-: | :-: | :-: |\n"

        for equipe in self.equipes:
            aux += str(equipe) + '\n'

        return aux
