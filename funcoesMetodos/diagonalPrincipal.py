import matriz

num_linhas = int(input("Digite o número de linhas da matriz: "))
num_colunas = int(input("Digite o número de colunas da matriz: "))
numInicial = int(input("Digite o número inicial da matriz: "))
numFinal = int(input("Digite o número final da matriz: "))

mat = matriz.geraMatriz(num_linhas, num_colunas, numInicial, numFinal)

print(mat)
print(matriz.caculaTracoMatriz(mat, num_linhas, num_colunas))
