from datetime import datetime

class Locadora:
    def __init__(self, preco_hora=3):
        self.jogos_alugados = {}  
        self.preco_hora = preco_hora

    def alugar_jogo(self, cliente, jogo):
        if cliente in self.jogos_alugados:
            print(f"⚠️ {cliente} já está com um jogo alugado.")
        else:
            self.jogos_alugados[cliente] = (jogo, datetime.now())
            print(f"✅ {cliente} alugou '{jogo}' às {self.jogos_alugados[cliente][1].strftime('%H:%M:%S')}")

    def devolver_jogo(self, cliente):
        if cliente not in self.jogos_alugados:
            print(f"❌ Nenhum jogo alugado por {cliente}.")
        else:
            jogo, hora_retirada = self.jogos_alugados.pop(cliente)
            tempo_uso = datetime.now() - hora_retirada
            horas = tempo_uso.total_seconds() / 3600
            valor = self.preco_hora * round(horas)
            print(f"🎮 {cliente} devolveu '{jogo}' após {horas:.2f}h. Total: R$ {valor:.2f}")
