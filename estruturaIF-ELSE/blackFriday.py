preco=float(input("Informe o preço do produto: "))
pagamento=input("Informe o metodo de pagamento(vista, debito, credito): ")

if pagamento=="vista":
    print("O preço total é: ",preco*.85)
elif pagamento=="debito":
    print("O preço total é: ",preco*.9)
elif pagamento=="credito    ":
    print("O preço total é: ",preco*.95)
else:
    print("Método de pagamento inválido!")