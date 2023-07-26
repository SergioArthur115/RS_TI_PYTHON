salario=float(input("Informe o salario: "))
cargo=input("Informe o cargo: ")

if cargo=="Programador de Sistemas":
    print(f"Seu novo salario é: {(salario*1.3):.2f}")
elif cargo=="Analista de Sistemas":
    print(f"Seu novo salario é: {(salario*1.2):.2f}")
elif cargo=="Analista de Banco de Dados":
    print(f"Seu novo salario é: {(salario*1.15):.2f}")
else:
    print("Cargo inválido!")