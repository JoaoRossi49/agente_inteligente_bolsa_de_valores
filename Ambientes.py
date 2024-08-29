class Ambiente():
    def __init__(self, estadoInicial=None):
        self.estado = estadoInicial
        self.objetosAmbiente = []
        self.agentes = []

    def percepcao(self, agente):
        return None

    def adicionaAgente(self, agente):
        self.agentes.append(agente)

    def adicionaObjeto(self, objeto):
        self.objetosAmbiente.append(objeto)


class AmbienteFinanceiro(Ambiente):
    def __init__(self, estadoInicial):
        super().__init__(estadoInicial)

    def percepcao(self, agente):
        for gst in self.estado:
            for i in self.agentes:
                agente.percepcao(i)
            return

    def executaAmbiente(self):
        for gst in self.estado:
            for ag in self.agentes:
                ag.atualizaEstado(gst)
                acaoComprar = ag.saida()
                if acaoComprar[0]:
                    ag.comprar()
                else:
                    ag.vender()

    def desempenhoAgentes(self):
        desempenho = []
        for i, ag in enumerate(self.agentes):
            desempenho.append((i, ag.desempenho()))
        return desempenho