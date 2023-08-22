def calculoFatorial(num):
    fatorial = 1
    for i in range(1, num+1):
        fatorial *= i
    return fatorial
num = int(input("Digite um numero: "))
print("O resultado é: ",calculoFatorial(num))