termo1=int(input("Informe o 1º termo de P.A: "))
num_termo=int(input("Informe o números de termos de P.A: "))
razao=int(input("Informe a razãp de P.A: "))

anterior = termo1
print(termo1)
for i in range(num_termo-1):
    termo=anterior+razao
    print(termo)
    anterior=termo