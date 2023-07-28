qtdM18 = 0
qtdF = 0
while True:
    idade = int(input("Informe a idade: "))
    if idade < 0:
        break
    else:
        sexo = input("Informe o sexo biologico(f ou m): ")

        if idade > 18 and sexo == "m" or sexo == "M":
            qtdM18 += 1
        if sexo == "f" or sexo == "F":
            qtdF += 1
print("Quantidade de homens acima de 18 anos: ", qtdM18)
print("Quantidade de mulheres de qualquer idade: ", qtdF)
