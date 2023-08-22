import math
def calculaAreaCirculo():
    r = float(input("Digite o raio do círculo: "))
    return math.pi * math.pow(r, 2)


def calculaAreaTriangulo():
    b = float(input("Digite a base do triângulo: "))
    h = float(input("Digite a altura do triângulo: "))
    return (b*h)/2


def calculaAreaRetangulo():
    b = float(input("Digite a base do retângulo: "))
    h = float(input("Digite a altura do retângulo: "))
    return b*h