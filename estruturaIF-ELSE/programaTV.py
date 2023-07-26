sobrenome = input("Informe o sobrenome de um dos apresentadores: ")

if sobrenome.upper() == "PINHEIRO" or sobrenome.upper() == "ARAÚJO":
    print("O programa é: Bom Dia Nação")
elif sobrenome.upper() == "BONNER" or sobrenome.upper() == "VASCONCELOS":
    print("O programa é: Jornal Brasileiro")
else:
    print("Apresentador(a) desconhecido(a)!")
