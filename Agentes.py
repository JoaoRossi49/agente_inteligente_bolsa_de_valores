class Agente():
    def __init__ (self, estado=None, funcaoAgente=None):
        if funcaoAgente == None:
            def funcaoAgente(*entradas):
                return "Ação Default"
        self.estado = estado
        self.funcaoAgente = funcaoAgente
        self.historicoPercepcoes = []

    def percepcao(self):
        entrada = input("Entre com um dado")
        self.historicoPercepcoes.append(eval(entrada))

    def saida(self):
        return self.funcaoAgente(self.historicoPercepcoes)
    
class AgenteNegociador(Agente):
    def __init__(self, estadoInicial = None, funcaoAgente = None):
        super().__init__(estadoInicial, funcaoAgente)
        self.observacao = 0
        self.mediaAtual = 0
        self.medias = []

    def atualizaEstado(self, valor):
        self.observacao += 1
        if self.observacao == 1:
            self.mediaAtual = valor
        else:
            self.mediaAtual = self.mediaAtual + (valor - self.mediaAtual) / (self.observacao + 1)
            #self.mediaAtual = self.estado[-1] / len(self.medias)
        self.estado.append(valor)
        self.medias.append(self.mediaAtual)

    def percepcao(self, cotacaoAtual):
        self.atualizaEstado(cotacaoAtual)

    def saida(self):
        return self.funcaoAgente(self.medias, self.estado[-1])
    
class AgenteDesempenho(AgenteNegociador):
    def __init__(self, estadoInicial, funcaoAgente = None, SaldoR=0, SaldoA=0):
        super().__init__(estadoInicial, funcaoAgente)
        self.SaldoReal = SaldoR
        self.SaldoAtivo = SaldoA
        self.evolucao = []

    def comprar(self):
        #Saldo real:  1000 Saldo ativo:  0 Ultimo estado:  16.27
        if self.SaldoReal > 0:
            self.SaldoAtivo += self.SaldoReal / self.estado[-1]
            self.SaldoReal = 0

    def vender(self):
        if self.SaldoAtivo > 0:
            self.SaldoReal += self.SaldoAtivo * self.estado[-1]
            self.SaldoAtivo = 0
        self.evolucao.append(self.SaldoReal)

    def desempenho(self):
        return self.evolucao[-1] - self.evolucao[0]
