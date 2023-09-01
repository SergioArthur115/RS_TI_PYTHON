from classes import PontoModificado as Ponto

pA = Ponto("A", 100, 200)
pB = Ponto("B", 120, 150)
pC = Ponto("C",  50,  95)
pD = Ponto("D", 199,  54)

print(pA)
print(pB)
print(
    f"Distância entre {pA.nome} e {pB.nome}: {pA.calcularDistancia(pB):.2f} \n")

print(pC)
print(pD)
print(
    f"Distância entre {pC.nome} e {pD.nome}: {pC.calcularDistancia(pD):.2f} \n")
