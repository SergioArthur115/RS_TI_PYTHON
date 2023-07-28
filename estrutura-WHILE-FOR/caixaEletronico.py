nome=input("Informe seu nome: ")
i = 3
while i > 0:
    senha=input("Informe sua senha: ")
    if senha=="123456":
        print(f"Olá,{nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        i-=1
        print(f"Senha incorreta! Você tem {i} tentativas.")
        if i==0:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
            break