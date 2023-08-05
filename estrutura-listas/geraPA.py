primeiro_termo = int(input("Digite o primeiro termo da PA: "))
qtd_termos = int(input("Digite a quantidade de termos da PA: "))
razao = int(input("Digite a razão da PA: "))

termos = []
soma = 0
for i in range(qtd_termos):
    termo = primeiro_termo + i * razao
    termos.append(termo)
    soma += termo

print("Termos da PA:", termos)
print("Soma dos elementos da PA:", soma)