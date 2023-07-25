print("**** TABELA VERDADE ****")
print("1. Operador AND")
print("2. Operador OR")
print("3. Operador NOT")
print("**************************")
op=int(input("Escolha a opção: "))
if op==1 or op==2:
    bit1=int(input("Informe o primeiro bit: "))
    bit2=int(input("Informe o segundo bit: "))
    if op==1:
        if bit1==1 and bit2==1:
            print("O resultado foi 1")
        else:
            print("O resultado foi 0")
    else:
        if bit1==0 and bit2==0:
            print("O resultado foi 0")
        else:
            print("O resultado foi 1")
else:
    bit1=int(input("Informe o bit: "))
    if bit1==1:
        print("O resultado foi 0")
    else:
        print("O resultado foi 1")