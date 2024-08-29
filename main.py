from cotacoes import get_cotacoes
from Agentes import *
from Ambientes import *
import matplotlib.pyplot as plt

x, y = get_cotacoes()

def funcaoAgenteCompraAcao_new(medias, media, cotacao):
    media_de_medias = sum(medias)/len(medias)
    if cotacao >= media_de_medias:
        return False, cotacao, media_de_medias
    else:
        return True, cotacao, media_de_medias

def funcaoAgenteCompraAcao_old(medias, media, cotacao):
    if cotacao >= media:
        return False, cotacao, media
    else:
        return True, cotacao, media


ag = AgenteDesempenho([], funcaoAgenteCompraAcao_old, 1000, 0)
ag2 = AgenteDesempenho([], funcaoAgenteCompraAcao_new, 1000, 0)
amb = AmbienteFinanceiro(y)
amb.adicionaAgente(ag)
amb.adicionaAgente(ag2)
amb.executaAmbiente()
desempenho = amb.desempenhoAgentes()
print(f'O desempenho dos agentes informados foram: {desempenho}')

# Evolução do Desempenho
x2 = list(range(len(ag.evolucao)))
x2ag2 = list(range(len(ag2.evolucao)))
plt.plot(x2, ag.evolucao, label='Agente antigo')
plt.plot(x2ag2, ag2.evolucao, label='Agente novo')
plt.xlabel("Transações")
plt.ylabel("Saldo em Reais")
plt.title("Evolução do agente")
plt.legend()
plt.show()