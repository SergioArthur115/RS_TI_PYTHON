from Cliente import Cliente

class Conta:
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def exibirSaldo(self):
        print(f"Conta: {self.numero}")
        print(f"Cliente: {self.cliente}", end="")
        if type(self.cliente) is list:
            for cliente in self.cliente:
                print(f"Cliente: {self.cliente[cliente]} | ", end=" ")
        else:
            print(self.cliente.nome, end=" | ")
        print(f"Saldo: {self.saldo:.2f} \n")
            
                

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

class ContaBancaria:
    pass
