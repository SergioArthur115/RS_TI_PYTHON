class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def exibirSaldo(self):
        print(f"Conta: {self.numero} || ", end="")
        print(f"Cliente: {self.cliente}")
        print(f"Saldo: {self.saldo:.2f}\n")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

class ContaBancaria:
    pass
