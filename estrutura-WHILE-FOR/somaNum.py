a = int(input("Informe A: "))
b = int(input("Informe B: "))

if a < b:
    soma = 0
    for i in range(a, b+1):
        soma += 1
        print("Soma: ", soma)
else:
    print("Error")
