from random import randrange 

lin=int(input("Informe o número de linhas das matrizes: "))
col=int(input("Informe o número de colunas das matrizes: "))
A=[[randrange(1,11) for i in range(col)] for j in range(lin)]
B=[[randrange(1,11) for i in range(col)] for j in range(lin)]

baixodp=0
cimadp=0
for i in range(lin):
    for j in range(col):
        if i < j:
            cimadp+=B[i][j]
        if i > j:
            baixodp+=A[i][j]

soma=baixodp+cimadp         

print("Matriz A:")
for i in range(lin):
    for j in range(col):
        print(A[i][j], end=' ')
    print()
print("Matriz B:")
for i in range(lin):
    for j in range(col):
        print(B[i][j], end=' ')
    print()


print("Soma: ",soma)