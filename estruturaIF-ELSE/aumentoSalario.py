salario=float(input("Informe o salario: "))
cargo=input("Informe o cargo: ")

if cargo=="Programador de Sistemas":
    print("Seu novo salario é: ",salario*1.3)
elif cargo=="Analista de Sistemas":
    print("Seu novo salario é: ",salario*1.2)
elif cargo=="Analista de Banco de Dados":
    print("Seu novo salario é: ",salario*1.15)
else:
    print("Cargo inválido!")