import random

alunos=["Luis","Luis","Marcelo","Arthur","Gustavo","Matheus"]
random.shuffle(alunos)
print(alunos)
sorteada = random.choice(alunos)
print(sorteada)
alunos.sort()
print(alunos)
alunos.sort(reverse=True)
print(alunos)
alunos.remove("Luis")
print(alunos)
alunos.pop(1)
print(alunos)
alunos.pop()
print(alunos)
del alunos[1]
print(alunos)
del alunos
print(alunos)