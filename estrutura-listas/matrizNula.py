import random

num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))
matriz = []

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        num = random.random()
        linha.append(num)
    matriz.append(linha)

texto="A matriz é nula."
for linha in matriz:
    for num in linha:
        if num != 0:
            texto="A matriz não é nula."

print(matriz)
print(texto)