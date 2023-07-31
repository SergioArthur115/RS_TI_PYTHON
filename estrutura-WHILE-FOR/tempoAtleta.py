atletas = []
tempos = []
soma = 0
melhor = 0
pior = 0
qtdAtleta=0

for i in range(7):
    atleta = input("Informe o nome do atleta: ")
    atletas.append(atleta)
    
    tempo = float(input("Informe o seu tempo: "))
    tempos.append(tempo)
    
    if i == 0:
        melhor = atleta
        pior = atleta
    else:
        if tempo < tempos[i-1]:
            melhor = atleta
        elif tempo >tempos[i-1]:
            pior = atleta
    if tempo > 12 and tempo <15:
        qtdAtleta+=1
    soma += tempo

print("O melhor atleta é: ", melhor)
print("O pior atleta é: ", pior)
print("A média é:", soma/7)
print("A quantidade de atletas com o tempo entre 12 e 15 segundos é:", qtdAtleta)
