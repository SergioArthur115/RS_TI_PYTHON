peso=float(input("Informe o seu peso: "))
altura=float(input("Informe a sua altura: "))
imc=peso/(altura*altura)
print("IMC: ",imc)
if imc<18.5:
    print("Abaixo do peso")
elif imc<25:
    print("Peso normal")
elif imc<30:
    print("Sobrepeso")
elif imc<35:
    print("Obesidade grau 1")
elif imc<40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")