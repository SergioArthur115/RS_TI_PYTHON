import math

x1=float(input("Informe A x1: "))
y1=float(input("Informe A y1: "))
x2=float(input("Informe B x2: "))
y2=float(input("Informe B y2: "))
x3=float(input("Informe C x3: "))
y3=float(input("Informe C y3: "))

dA=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
dC=math.sqrt(math.pow(x3-x1,2)+math.pow(y3-y1,2))
dB=math.sqrt(math.pow(x3-x2,2)+math.pow(y3-y2,2))

status1=False
status2=False
status3=False

if dA>0 and dC>0 and dB>0:
    if dB-dC<dA and dB-dC <dB+dC:
        status1=True
    if dA-dC<dB and dA-dC< dA+dC:
        status2=True
    if dA-dB<dC and dA-dB<dA+dB:
        status3=True
if status1 and status2 and status3:
    print("É triangulo")
    if(dA==dB==dC):
        print("É Equilátero!")
    elif(dA!=dB!=dC):
        print("É Escaleno!")
    else:
        print("É Isósceles!")
else:
    print("Não é triangulo")