num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        num = int(input(f"Digite o elemento da posição ({i+1}, {j+1}): "))
        linha.append(num)
    matriz.append(linha)

linhas = len(matriz)
colunas = len(matriz[0])
texto="A matriz é uma matriz diagonal."
if linhas != colunas:
    texto="A matriz não é uma matriz diagonal."

for i in range(linhas):
    for j in range(colunas):
        if i != j and matriz[i][j] != 0:
            texto="A matriz não é uma matriz diagonal."

print(matriz)
print(texto)