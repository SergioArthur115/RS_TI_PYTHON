import math

class Ingresso:

    def __init__(self, evento, valor):
        self.evento = evento
        self.valor = valor

    def exibirValor(self):
        return self.valor

    def __str__(self):
        return f"{self.evento}: R$ {self.valor:.2f}"

class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return 2*(self.largura + self.altura)

    def calcularArea(self):
        return self.altura * self.largura

class Ponto:

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.nome}: ({self.x}, {self.y})"

class Lista:
    def __init__(self, elementos):
        self.itens = elementos

    def exibirListaDistinta(self):
        novaLista = []
        for item in self.itens:
            if item not in novaLista:
                novaLista.append(item)
        return novaLista

class Calculadora:

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def somar(self):
        return self.op1 + self.op2

    def subtrair(self):
        return self.op1 - self.op2

    def multiplicar(self):
        return self.op1 * self.op2

    def dividir(self):
        return self.op1 / self.op2

    def potencia(self):
        return self.op1 ** self.op2

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentagem):
        return self.salario + (self.salario * porcentagem / 100)

class Carro:

    def __init__(self, consumo):
        self.consumo = consumo
        self.combustível = 0

    def abastecer(self, litros):
        self.combustível += litros

    def exibirCombustivel(self):
        print(f"Combustível: {self.combustível:.1f} litros")

    def andar(self, distancia):
        print(f"O carro andou: {distancia} km")
        litrosGastos = distancia / self.consumo
        self.combustível -= litrosGastos

class ContaInvestimento:

    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    def adicionarJuros(self):
        self.saldo += (self.saldo * self.taxaJuros / 100)

class Trigonometria:

    def __init__(self, angulo):
        self.anguloGraus = angulo
        self.anguloRad = math.radians(angulo)

    def seno(self):
        return math.sin(self.anguloRad)

    def cosseno(self):
        return math.cos(self.anguloRad)

    def tangente(self):
        return math.tan(self.anguloRad)

    def __str__(self):
        return f"\n - Ângulo em graus: {self.anguloGraus} \n" \
               f"\n - Ângulo em radianos: {self.anguloRad:.4f}\n" \
               f"\n - Seno: {self.seno():.4f}\n" \
               f"\n - Cosseno: {self.cosseno():.4f}\n" \
               f"\n - Tangente: {self.tangente():.4f} "

class PontoModificado():

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def calcularDistancia(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self):
        return f"{self.nome}: ({self.x}, {self.y})"