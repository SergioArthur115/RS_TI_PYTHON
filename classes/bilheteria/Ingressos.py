class Ingresso:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def exibirValor(self):
        return self.valor

    def __str__(self):
        return f"{self.nome}: R$ {self.valor:.2f}"
