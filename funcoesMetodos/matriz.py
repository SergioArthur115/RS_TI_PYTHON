import random



def geraMatriz(num_linhas,num_colunas,numInicial,numFinal):
    
    e = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            num = random.randint(numInicial,numFinal)
            linha.append(num)
        e.append(linha)
    return e
        
def caculaTracoMatriz(e,num_linhas,num_colunas):
    dp=0
    for i in range(num_linhas):
        for j in range(num_colunas):
            if i == j:
                dp+=e[i][j]
    return dp