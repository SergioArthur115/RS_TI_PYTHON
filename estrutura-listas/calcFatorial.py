while True:
    n = int(input("Digite um número ímpar maior que 1: "))
    if n > 1 and n % 2 != 0:
        break
    else:
        print("Número inválido. Tente novamente.")

numeros = []
for i in range(n):
    numero = int(input("Digite um número inteiro positivo: "))
    numeros.append(numero)

meio = numeros[n // 2]
fatorial=1
for i in range(1, meio+1):
    fatorial *= i

print("O fatorial do elemento selecionado é:", fatorial)