import math

num1 = float(input("Informe o numero 1 positivo: "))
num2 = float(input("Informe o numero 2 positivo: "))

print("Digite 1 para realizar a media ponderada")
print("Digite 2 para realizar o quadrado da soma dos 2 números")
print("Digite 3 para realizar cubo do menor número")
op=int(input("Escolha uma opção:"))

if op==1:
    print("A média ponderada é: ",(num1*2+num2*3)/5)
elif op==2:
    print("O quadrado da soma dos 2 números é: ",math.pow((num1+num2),2))
elif op==3:
    if num1<num2:
        num=num1
    else:
        num=num2
    print("O cubo do menor número é: ",math.pow(num,3))
else:
    print("Opção Invalida!!!")