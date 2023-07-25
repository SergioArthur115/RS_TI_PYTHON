estatura=[]

estatura.append(float(input("Informe estatura 1: ")))
estatura.append(float(input("Informe estatura 2: ")))
estatura.append(float(input("Informe estatura 3: ")))

estatura.sort()

if estatura[0]==estatura[1] or estatura[1]==estatura[2] or estatura[0]==estatura[2]:
    print("Há, pelo menos, 2 pessoas com a mesma estatura!")
else:
    print("Maior estatura: ",estatura[2])
    