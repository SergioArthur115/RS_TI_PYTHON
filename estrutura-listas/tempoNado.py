nomes = []
tempos = []

for i in range(7):
    nome = input("Digite o nome do nadador: ")
    tempo = float(input("Digite o tempo (em segundos) do nadador: "))
    nomes.append(nome)
    tempos.append(tempo)

melhor = min(tempos)
indice_melhor = tempos.index(melhor)
nadador_melhor = nomes[indice_melhor]
pior = max(tempos)
indice_pior = tempos.index(pior)
nadador_pior = nomes[indice_pior]
media = sum(tempos) / len(tempos)

print("Nadador com o melhor tempo:", nadador_melhor)
print("Nadador com o pior desempenho:", nadador_pior)
print("Tempo médio dos nadadores:", media, "segundos")
