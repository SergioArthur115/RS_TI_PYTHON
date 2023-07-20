qtdCamisa = int(input("Informe a quantidade de camisas a serem compradas: "))
if qtdCamisa < 5:
    total = (qtdCamisa*78.5)*.97
elif qtdCamisa < 10:
    total = (qtdCamisa*78.5)*.95
else:
    total = (qtdCamisa*78.5)*.93
print(f"Total a pagar: {total:.2f}")