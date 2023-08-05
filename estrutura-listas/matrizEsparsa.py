num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        num = int(input(f"Digite o elemento da posição ({i+1}, {j+1}): "))
        linha.append(num)
    matriz.append(linha)

zeros = 0
elementos = 0
for linha in matriz:
    for elemento in linha:
        elementos += 1
        if elemento == 0:
            zeros += 1
texto="A matriz não é uma matriz esparsa."
if zeros > elementos / 2:
    texto="A matriz é uma matriz esparsa."

print(matriz)
print(texto)