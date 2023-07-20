nome = input("Digite seu nome completo: ")
if len(nome) > 50:
    print("Seu nome é grande, ele posssui mais de 50 letras.")

    print(f"Ele possui {len(nome)} caracteres.")
    
    
valor=10
if valor:
    print("Valor é diferente de zero => verdade.")


valor=0
if not valor:
    print("Valor é false, mas o not inverte o resultado.")


valor = int(input("Informe um numero: "))
if valor % 2 == 0:
    print("O valor é par")
else:
    print("O valor é impar")