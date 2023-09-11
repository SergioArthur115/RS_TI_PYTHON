import tkinter as tk


class Tela:

    def __init__(self, master):
        self.nossaTela = master

        self.frame = tk.Frame(self.nossaTela)
        self.frame.pack(ipadx=30, ipady=30)
        self.frame2 = tk.Frame(self.nossaTela)
        self.frame2.pack(ipadx=30, ipady=30)
        self.frame3 = tk.Frame(self.nossaTela)
        self.frame3.pack(ipadx=30, ipady=30)
        self.frame4 = tk.Frame(self.nossaTela)
        self.frame4.pack(ipadx=30, ipady=30)
        self.frame5 = tk.Frame(self.nossaTela)
        self.frame5.pack(ipadx=30, ipady=30)

        self.lb1 = tk.Label(self.frame, text="Informe o nome: ")
        self.lb1.pack(side=tk.LEFT)
        self.lb2 = tk.Label(self.frame2, text="Informe o telefone: ")
        self.lb2.pack(side=tk.LEFT)
        self.lb3 = tk.Label(self.frame3, text="Informe o Email: ")
        self.lb3.pack(side=tk.LEFT)
        self.lb4 = tk.Label(self.frame4, text="Informe o usuário: ")
        self.lb4.pack(side=tk.LEFT)
        self.lb5 = tk.Label(self.frame5, text="Informe a senha: ")
        self.lb5.pack(side=tk.LEFT)

        self.entrada1 = tk.Entry(self.frame)
        self.entrada1.pack(side=tk.LEFT, padx=20)
        self.entrada2 = tk.Entry(self.frame2)
        self.entrada2.pack(side=tk.LEFT, padx=20)
        self.entrada3 = tk.Entry(self.frame3)
        self.entrada3.pack(side=tk.LEFT, padx=20)
        self.entrada4 = tk.Entry(self.frame4)
        self.entrada4.pack(side=tk.LEFT, padx=20)
        self.entrada5 = tk.Entry(self.frame5)
        self.entrada5.pack(side=tk.LEFT, padx=20)

        self.btn = tk.Button(self.nossaTela, text="Cadastrar", bg='red',command=self.cadastrar)
        self.btn.pack()

        self.saida = tk.Label(self.nossaTela, font=('Arial', 16))
        self.saida.pack(pady=15)
    
    def cadastrar(self):
        nome = self.entrada1.get()
        telefone = self.entrada2.get()
        email = self.entrada3.get()
        usuario = self.entrada4.get()
        senha = self.entrada5.get()

        print("Nome: ",nome)
        print("Telefone: ",telefone)
        print("Email: ",email)
        print("Usuário: ",usuario)
        print("Senha: ",senha)


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()