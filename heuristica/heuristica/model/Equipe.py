from model.Maquina import Maquina


def eh_maquina(elemento):
    return True if isinstance(elemento, Maquina) else False


class Equipe:

    # construtor
    def __init__(self, id,  disponibilidade, janela_final: list, janela_inicial: list):
        self.id = id
        self.disponibilidade = disponibilidade
        self.janela_final = janela_final.copy()
        self.janela_inicial = janela_inicial.copy()
        # TODO ajustar tempo de processamento para um cálculo
        self.tempo_de_processamento = 0
        self.maquinas = []

    def adiciona_maquina(self, nova_maquina):
        if not eh_maquina(nova_maquina):
            return

        self.maquinas.append(nova_maquina)
        self.__ajusta_janela_inicial__(nova_maquina)
        self.__ajusta_tempo_janela_final__(nova_maquina)
        self.__ajusta_tempo_disponibilidade__(nova_maquina)

    # ------------------------------------------

    def __ajusta_tempo_janela_final__(self, nova_maquina):
        self.janela_final[nova_maquina.index] -= nova_maquina.tempo_processamento

    # ------------------------------------------

    def __ajusta_tempo_disponibilidade__(self, nova_maquina):
        self.disponibilidade -= nova_maquina.tempo_processamento

    # ------------------------------------------

    def __ajusta_janela_inicial__(self, nova_maquina):

        index_maquina = nova_maquina.index
        janela = nova_maquina.tempo_processamento
        horario_autorizado = self.janela_inicial[index_maquina]
        tempo_atual = self.tempo_de_processamento

        # precisa esperar ?
        tempo_ajustado = max(tempo_atual, horario_autorizado) + janela
        self.tempo_de_processamento = tempo_ajustado

    # ------------------------------------------

    def liberar_maquinas_para_troca(self):
        for maquina in self.maquinas:
            maquina.desmarcar()

    # ------------------------------------------

    def existe_equipe_valida(self):
        for maquina in self.maquinas:
            if not maquina.invalida:
                return True

        return False

    # ------------------------------------------

    def __str__(self):
        aux = f'EQUIPE # {self.id}\n'
        aux += f'DISPONIBILIDADE: {self.disponibilidade}\n'
        aux += f'TEMPO TOTAL {self.tempo_de_processamento}\n'
        aux += 'MAQUINAS: \n'

        for maquina in self.maquinas:
            aux += '\t' + str(maquina) + '\n'

        return aux
