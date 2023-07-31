countMedia=0
for i in range(5):
    nota1=0
    nota2=0
    media=0
    nome = input("Informe o nome do aluno: ")
    nota1 = float(input(f"Informe a 1ª nota do {nome}: "))
    nota1 = float(input(f"Informe a 2ª nota do {nome}: "))
    media=(nota1+nota2)/2
    if media >= 2 and media <6:
        countMedia += 1
result=countMedia*20
print(f"Alunos em prova final: {result} %")