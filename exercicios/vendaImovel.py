nome=input("Informe o nome do corretor: ")
qtdImovel=int(input("Informe quantidade de imoveis vendidos: "))
totalVenda=float(input("Informe o valor total de vendas: "))
salario=1500.00+(qtdImovel*200.00)+(totalVenda*0.05)
print(f"Salario: {salario:.2f}")