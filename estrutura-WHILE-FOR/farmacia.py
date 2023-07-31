medicamentos = []
preco = []
soma = 0
barato = 0

for i in range(5):
    medicamento = input("Informe o nome do medicamento: ")
    medicamentos.append(medicamento)
    
    preco_medicamento = float(input("Informe o preço do medicamento: "))
    preco.append(preco_medicamento)
    
    if i == 0:
        barato = medicamento
    else:
        if preco_medicamento < preco[i-1]:
            barato = medicamento
    
    soma += preco_medicamento

print("O produto mais barato é: ", barato)
print("A média é:", soma/5)
