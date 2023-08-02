idade = []

idades = [22, 56, 50, 30, 20, 25, 15, 16]

aluno = ["Fulano de tal", 0, 1.80, True]

print(f"Nome: {aluno[0]}")
print(f"Nº de filhos: {aluno[1]}")
print(f"altura: {aluno[2]}")
print(f"Passaporte: {aluno[3]}")

alunos=["Marcelos dos tocos","Luís","Sergio","Luiz"]
alunos.append("Gustavo")
print(alunos)
#while True:
#    alunos.append(input("Informe o nome do aluno: "))
#    nome=input("Informe o nome do aluno: ")
#    pos=int(input("Informe a posição do aluno: "))
#    alunos.insert(nome,pos)
#    
#    resp = input("Deseja continuar? s/n: ")
#    if resp.upper() == "N":
#        break
#print(alunos)

copia =list(alunos)

if copia == alunos:
    alunos.clear()
    print("Lista de alunos esvaziada")
else:
    print("Erro: Cópia gerada não é igual à original")
    
lista1=["Marcelos dos tocos","Luís","Sergio","Luiz"]
lista2=["Luis","Luis","Marcelo","Arthur","Gustavo","Matheus"]
lista3=lista1+lista2
print(lista3)

ocorrencias = lista3.count("Luis")
print(ocorrencias)
tamanho=len(lista3)
print(tamanho)

idades = [22, 56, 50, 30, 20, 25, 15, 16]
menor=min(idades)
maior=max(idades)
media=sum(idades)/len(idades)

print(idades)
print(menor)
print(maior)
print(media)

pesquisa ="Matheus"
if pesquisa in lista3:
    indice = lista3.index(pesquisa)
    print(pesquisa,indice)
else:
    print("Não esta na lista")
    
for indice,nome in enumerate(lista3):
    print(indice,nome)