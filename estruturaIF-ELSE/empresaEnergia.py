print("********************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("********************************")
print("1-Tensão (em  Volt)")
print("2-Tensão (em  Volt)")
print("3-Tensão (em  Volt)")
print("********************************")
opcao = int(input("Qual grandeza deseja calcular?"))
if opcao == 1:
    resistencia = float(input("Informe a resistencia: "))
    corrente = float(input("Informe a corrente: "))
    tensao = resistencia*corrente
    print(f"A tensão é {tensao:.2f}")
elif opcao == 2:
    tensao = float(input("Informe a tensão: "))
    corrente = float(input("Informe a corrente: "))
    resistencia = tensao/corrente
    print(f"A resistencia é {resistencia:.2f}")
elif opcao == 3:
    tensao = float(input("Informe a tensão: "))
    resistencia = float(input("Informe a resistencia: "))
    corrente = tensao/resistencia
    print(f"A corrente é {corrente:.2f}")