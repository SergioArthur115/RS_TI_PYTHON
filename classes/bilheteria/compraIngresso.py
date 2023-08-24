from Ingressos import Ingresso

evento1 = Ingresso("Mirage e Circo", 100.00)
evento2 = Ingresso("Cirque du Soleil", 800.00)
evento3 = Ingresso("Concerto a luz de vela", 30)

print(evento1)
print(evento2)
print(evento3)
print("-----------------------")
print(evento1.exibirValor())
print(evento2.exibirValor())
print(evento3.exibirValor())
print("----------------------")
print(evento1.__str__())
print(evento2.__str__())
print(evento3.__str__())
