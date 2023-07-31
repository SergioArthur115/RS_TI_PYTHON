op=99
salariosEnfer=[]
salariosNutri=[]
salariosMed=[]
mediaNutri=0
qtdMed4500=0
while op !=0:
    print("------------------")
    print("Digite 1 para Enfermeiro")
    print("Digite 2 para Nutricionista")
    print("Digite 3 para Médico")
    print("Digite 0 para Sair")
    print("------------------")
    op=int(input("Escolha a opção: "))
    if op==0:
        break
    salario=float(input("Informe o salario: "))
    if op==1:
        salariosEnfer.append(salario)
    elif op==2:
        salariosNutri.append(salario)
        mediaNutri+=salario
    elif op==3:
        salariosMed.append(salario)
        if salario > 4500:
            qtdMed4500+=1
    else:
        print("Opção Inválida!!!")
if mediaNutri:
    mediaNutri=mediaNutri/len(salariosNutri)

print("A média salarial dos nutricionistas é: ",mediaNutri)
print("O número de médicos com sálario maior que 4500 é: ",qtdMed4500)