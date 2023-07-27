num = int(input("Informe a quantidade de números: "))
soma=0
for i in range(num):
    n = float(input("Informe um número: "))
    soma+=n
media=soma/num
print(f"Média: {media:.2f}")



num = int(input("Informe a quantidade de números: "))
x=0
while x<=num:
    n = float(input("Informe um número: "))
    soma+=n
    x+=1
media=soma/num
print(f"Média: {media:.2f}")