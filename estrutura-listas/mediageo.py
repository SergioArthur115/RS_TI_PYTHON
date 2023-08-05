import math

numeros = []
n = int(input("Digite a quantidade de números da lista: "))
for i in range(n):
    elemento = float(input("Digite o numero {}: ".format(i+1)))
    numeros.append(elemento)

menor = min(numeros)
maior = max(numeros)
media_geometrica = math.sqrt(menor * maior)

print("A média geométrica entre o menor elemento ({}) e o maior elemento ({}) é: {}".format(menor, maior, media_geometrica))