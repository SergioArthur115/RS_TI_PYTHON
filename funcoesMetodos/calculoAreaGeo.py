import calcArea

print("1 - Círculo")
print("2 - Triângulo")
print("3 - Retângulo")

op = int(input("Qual figura deseja calcular a área?: "))

if op == 1:
    print(f"A área do círculo é: {calcArea.calculaAreaCirculo():.2f}")
elif op == 2:
    print(f"A área do triângulo é: {calcArea.calculaAreaTriangulo():.2f}")
elif op == 3:
    print(f"A área do retângulo é: {calcArea.calculaAreaRetangulo():.2f}")
else:
    print("ERROR!!!")
