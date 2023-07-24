estatura=[]

estatura.append(float(input("Informe estatura 1: ")))
estatura.append(float(input("Informe estatura 2: ")))
estatura.append(float(input("Informe estatura 3: ")))

estatura.sort()

print("Estatura em ordem crescente: ",estatura)
print("Menor estatura: ",estatura[0])
print("Maior estatura: ",estatura[2])
print("Estatura media: ",estatura[1])