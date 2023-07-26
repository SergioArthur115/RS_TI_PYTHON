import math


a=float(input("Informe a constante A: "))
b=float(input("Informe a constante B: "))
c=float(input("Informe a constante C: "))

if((math.pow(b,2)-4*a*c)>0):
    x1=(-b + math.sqrt(math.pow(b,2)-4*a*c))/2*a
    x2=(-b - math.sqrt(math.pow(b,2)-4*a*c))/2*a
    print("x1: ", x1)
    print("x2: ", x2)
elif((math.pow(b,2)-4*a*c)==0):
    x1=(-b + math.sqrt(math.pow(b,2)-4*a*c))/2*a
    print("x: ", x1)
else:
    print("ERROR!")