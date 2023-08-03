from random import randrange 

lin=int(input("Informe o número de linhas da matriz: "))
col=int(input("Informe o número de colunas da matriz: "))
A=[[randrange(1,11) for i in range(col)] for j in range(lin)]

texto=("É uma matriz triangular inferior")
if lin != col:
    texto=("Não é uma matriz triangular inferior")
else:
    for i in range(lin):
        for j in range(col):
            if i < j:
                if(A[i][j]!=0):
                    texto=("Não é uma matriz triangular inferior")
                    break

print("Matriz A:")
for i in range(lin):
    for j in range(col):
        print(A[i][j], end=' ')
    print()
print(texto)