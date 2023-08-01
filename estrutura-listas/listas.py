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
while True:
    alunos.append(input("Informe o nome do aluno: "))
    nome=input("Informe o nome do aluno: ")
    pos=int(input("Informe a posição do aluno: "))
    alunos.insert(nome,pos)
    
    resp = input("Deseja continuar? s/n: ")
    if resp.upper() == "N":
        break
print(alunos)