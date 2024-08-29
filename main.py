from cotacoes import get_cotacoes
from Agentes import *
from Ambientes import *

x, y = get_cotacoes()

def funcaoAgenteCompraAcao(medias, cotacao):
    media = sum(medias)/len(medias)
    if cotacao >= media:
        return False, cotacao, media
    else:
        return True, cotacao, media

ag = AgenteDesempenho([], funcaoAgenteCompraAcao, 1000, 0)
amb = AmbienteFinanceiro(y)
amb.adicionaAgente(ag)
amb.executaAmbiente()
desempenho = amb.desempenhoAgentes()
print(f'O desempenho do agente foi: {desempenho}')