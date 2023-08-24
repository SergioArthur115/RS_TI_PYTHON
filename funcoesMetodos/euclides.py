def mdc(a, b):
    while b != 0:
        print("A=",a)
        print("B=",b)
        a, b = b, a % b
        print("A=",a)
        print("B=",b)
        print("-----------------")
    return a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = mdc(num1, num2)
print("O máximo divisor comum é:", resultado)