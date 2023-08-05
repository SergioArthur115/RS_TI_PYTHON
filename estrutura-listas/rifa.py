import random

compradores = []

while True:
    nome = input("Digite o nome do comprador (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    compradores.append(nome)

if len(compradores) == 0:
    print("Nenhum comprador cadastrado.")
else:
    ganhador = random.choice(compradores)
    print("O ganhador do prêmio é:", ganhador)
