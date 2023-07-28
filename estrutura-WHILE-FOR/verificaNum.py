num=99
i=0
qtdPar=0
while num>5:
    num = int(input("Informe a quantidade de números: "))
    if num>5:
        print("A quantidade de números deve ser menor que 5")
while i<num:
    n = float(input("Informe um número: "))
    if(n%2==0):
        qtdPar+=1
    i+=1
print(f"A quantidade de números pares é: {qtdPar}")