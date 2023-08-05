import random
from math import pow

n = int(input("Digite um valor para N (N > 1): "))
numeros = [random.randint(1, 100) for _ in range(n)]

media = 1
for i in numeros:
    media *= i
media = pow(media, 1/len(numeros))

print("A média geométrica dos numeros da lista é:", media)